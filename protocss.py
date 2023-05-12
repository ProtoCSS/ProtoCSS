import os
import re
from watchdog.events import FileSystemEventHandler
from helper import protocss_dict
from colorama import Fore, Back, Style, init
from datetime import datetime

from helper.errors import ProtoCSSError

__version__ = "0.0.2"
class ProtoCSS:

    def __init__(self):
        self.shorthand_properties = protocss_dict.shorthand_properties
        self.pd_shorthand_properties = protocss_dict.pd_shorthand_properties
        self.lists = {}

    def replace_list_item(self, match):
        list_name, index = match.groups()
        index = int(index)
        if list_name in self.lists and index < len(self.lists[list_name]):
            return self.lists[list_name][index]
        return f"/* Error: Invalid list item 'list@{list_name}[{index}]' */"

    def convert(self, protocss: str, base_path: str = "static/") -> str:
        try:
            lines = protocss.split("\n")
            for line_number, line in enumerate(lines, start=1):
                try:
                    def process_import(match):
                        imported_file = match.group(1)

                        if imported_file.startswith("http://") or imported_file.startswith("https://"):
                            return f'@import url("{imported_file}");'
                        elif imported_file.endswith(".css"):
                            imported_file_path = os.path.join(f"{base_path}css/", imported_file)
                            if os.path.isfile(imported_file_path):
                                return f'@import url("{imported_file_path}");'
                            else:
                                raise ProtoCSSError(f"File '{imported_file}' not found in static/css/.")
                        elif imported_file.endswith(".ptcss"):
                            imported_file_path = os.path.join(f"{base_path}/", imported_file)
                            if os.path.isfile(imported_file_path):
                                # imported_file_content = read_protocss_file(imported_file_path)
                                # return imported_file_content
                                imported_file = imported_file.replace(".ptcss", ".css")
                                return f'@import url("static/css/{imported_file}");'
                            else:
                                raise ProtoCSSError(f"File '{imported_file}' not found in static/.")
                        elif imported_file.endswith(""):
                            imported_file_path = os.path.join(f"{base_path}", f"{imported_file}.ptcss")
                            if os.path.isfile(imported_file_path):
                                return f'@import url("{imported_file_path}");'
                            else:
                                raise ProtoCSSError(f"File '{imported_file}' not found in static/.")
                        else:
                            raise ProtoCSSError(f"Invalid import '{imported_file}'.")

                    protocss = re.sub(r'import\s+"([^"]+)";', process_import, protocss)

                    variable_pattern = re.compile(r"@!(\w+)\s*:\s*([^;]+);")
                    variables = dict(variable_pattern.findall(protocss))

                    # Convert ProtoCSS variables to CSS custom properties
                    css_vars = "\n".join([f"--{key}: {value};" for key, value in variables.items()])
                    protocss = re.sub(variable_pattern, "", protocss)
                    protocss = f":root {{\n{css_vars}\n}}\n\n" + protocss

                    # Replace variable usage
                    def replace_var(match):
                        var_name = match.group(1)
                        return f"var(--{var_name})"

                    protocss = re.sub(r"%!(\w+)", replace_var, protocss)

                    # extract group definitions and store them in a dictionary
                    group_pattern = re.compile(r"mixin@(\w+)\s*\{([^}]+)\}")
                    groups = {}
                    for match in group_pattern.findall(protocss):
                        mixin_name = match[0]
                        mixin_styles = match[1]
                        groups[mixin_name] = mixin_styles.strip()

                    def replace_mixin(match):
                        mixin_name = match.group(1)
                        if mixin_name not in groups:
                            raise ProtoCSSError(f"Mixin '{mixin_name}' not found.")
                        mixin_styles = groups[mixin_name]
                        # Expand shorthand properties within the group
                        for shorthand, full_property in self.shorthand_properties.items():
                            pattern = re.compile(rf"{shorthand}\s*:\s*(.+?);")
                            mixin_styles = pattern.sub(f"{full_property}: \\1;", mixin_styles)
                        return mixin_styles

                    protocss = re.sub(r"mixin@(\w+);", replace_mixin, protocss)
                    protocss = re.sub(group_pattern, "", protocss)  # Remove group declarations

                    # Process xshorthand properties
                    for xshorthand, full_property in self.pd_shorthand_properties.items():
                        pattern = re.compile(rf"{xshorthand};")  # Modify regex to match the xshorthand
                        protocss = pattern.sub(f"{full_property};", protocss)

                    # Process regular shorthand properties
                    for shorthand, full_property in self.shorthand_properties.items():
                        pattern = re.compile(rf"{shorthand}\s*:\s*(.+?);")
                        protocss = pattern.sub(f"{full_property}: \\1;", protocss)

                    def expand_media_query(match):
                        try:
                            conditions = match.group(1).split("+")
                            expanded_conditions = []
                            for condition in conditions:
                                expanded_condition = condition.strip()
                                for shorthand, full_property in self.shorthand_properties.items():
                                    pattern = re.compile(rf"{shorthand}\s*:\s*(.+)")
                                    expanded_condition = pattern.sub(f"{full_property}: \\1", expanded_condition)
                                expanded_conditions.append(expanded_condition)
                            conditions = " and ".join(expanded_conditions)
                            return f"@media {conditions} {{"
                        except:
                            raise ProtoCSSError(f"Invalid media query '{match.group(1)}'.")

                    protocss = re.sub(r"@mq\s+([^{}]+){", expand_media_query, protocss)

                    list_pattern = re.compile(r"list@(\w+)\s*:\s*\[([^\]]+)\]")

                    def replace_list(match):
                        list_name = match.group(1)
                        list_values = [value.replace(" ", "") for value in match.group(2).split(',')]

                        # Change this line to use the list name as the key in a dictionary
                        self.lists[list_name] = list_values

                        if list_name not in self.lists:
                            raise ProtoCSSError(f"List '{list_name}' not found.")
                        else:
                            return ""

                    protocss = re.sub(r"list@(\w+):\s*\[([^\]]+)\];", replace_list, protocss)
                    protocss = re.sub(list_pattern, "", protocss)

                    def replace_for_loop(match):
                        iterator_name = match.group(1)
                        list_name = match.group(2)
                        selector = match.group(3).replace("{" + iterator_name + "}", "{}")
                        property_block = [prop for prop in str(match.group(4)).split(";")]

                        prop_list = []
                        for prop in property_block:
                            prop_list.append(prop)

                        for_loop_result = ""
                        if list_name in self.lists:
                            for value in self.lists[list_name]:
                                clean_value = re.sub(r'\W+', '', value)
                                for_loop_result += f"{selector}-{clean_value} {{\n"
                                for prop in property_block:
                                    prop = prop.strip()
                                    for shorthand, full_property in self.shorthand_properties.items():
                                        if prop.startswith(shorthand):
                                            prop = prop.replace(shorthand, full_property)
                                    if prop:
                                        prop_name, prop_value = [p.strip() for p in prop.split(":")]
                                        prop_value = prop_value.replace(f"{{{iterator_name}}}", value)
                                        for_loop_result += f"   {prop_name}: {prop_value};\n"
                                for_loop_result += "}\n\n"
                            return for_loop_result
                        else:
                            raise ProtoCSSError(f"In loop: List '{list_name}' not found.")

                    protocss = re.sub(r"list@(\w+)\[(\d+)\]", self.replace_list_item, protocss)
                    for_pattern = re.compile(r"for\s+(\w+)\s+in\s+(\w+)\s+{\s+(.[^{]+)\s+{\s+((.|\n)+?);\s+}\s+};",
                                             re.MULTILINE)

                    protocss = re.sub(for_pattern, replace_for_loop, protocss)

                    return protocss
                except Exception as e:
                    # print("\n")
                    raise ProtoCSSError(f"An error occurred during conversion: {e}", line_number)

        except ProtoCSSError as e:
            print(e)
            return None

    class FileChangeHandler(FileSystemEventHandler):
        def __init__(self, converter):
            print(f"{Fore.LIGHTWHITE_EX}ProtoCSS v{__version__}{Style.RESET_ALL} - For more information {Fore.CYAN}https://protocss.dev{Style.RESET_ALL}\n")
            print(f"{Fore.CYAN} * Watching for changes...\n{Style.RESET_ALL}")
            self.converter = converter
            self.now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        def on_created(self, event):
            if not event.is_directory and event.src_path.endswith('.ptcss'):
                file_name = os.path.basename(event.src_path)
                print(
                    f" {Fore.LIGHTWHITE_EX}{self.now}{Fore.WHITE} - File{Style.RESET_ALL} {Fore.LIGHTWHITE_EX}{file_name} {Fore.WHITE}has been {Back.LIGHTWHITE_EX}{Fore.LIGHTBLUE_EX}  created  {Style.RESET_ALL}")
                self.process(event.src_path)

        def on_modified(self, event):
            if not event.is_directory and event.src_path.endswith('.ptcss'):
                file_name = os.path.basename(event.src_path)
                print(
                    f" {Fore.LIGHTWHITE_EX}{self.now}{Fore.WHITE} - File{Style.RESET_ALL} {Fore.LIGHTWHITE_EX}{file_name} {Fore.WHITE}has been {Back.GREEN}{Fore.LIGHTWHITE_EX}  modified  {Style.RESET_ALL}")
                self.process(event.src_path)

        def process(self, file_path):
            print(f" {Fore.BLUE}* Processing {file_path}")
            try:
                protoCSS = read_protocss_file(file_path)
                if protoCSS:
                    css = self.converter.convert(protoCSS)
                    if css is not None:
                        fn = os.path.splitext(os.path.basename(file_path))[0]
                        output_filename = f"static/css/{fn}.css"
                        write_css_file(output_filename, css)
                        print(
                            f"\n\t{Back.BLUE}{Fore.LIGHTWHITE_EX}\t{fn}.ptcss converted successfully to {output_filename}\t{Style.RESET_ALL}\n")
                    else:
                        print(f"\n {Fore.RED}Conversion failed for {file_path}\n\n")
                else:
                    print(
                        f"\n\t{Back.WHITE}{Fore.LIGHTWHITE_EX}\tNothing to convert in {file_path}\t{Style.RESET_ALL}\n")
            except ProtoCSSError as e:
                print(f" {Fore.RED}{e}")


def read_protocss_file(filename: str) -> str:
    print(f" {Fore.BLUE}* Reading {filename}")
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        raise ProtoCSSError(f"File '{filename}' not found.")
    except Exception as e:
        raise ProtoCSSError(f"An unexpected error occurred while reading '{filename}': {e}")


def write_css_file(filename: str, css: str) -> None:
    print(f" {Fore.BLUE}* Writing to {filename}")
    try:
        with open(filename, "w") as f:
            f.write(css)
    except Exception as e:
        raise ProtoCSSError(f"Error while writing to '{filename}': {e}")
