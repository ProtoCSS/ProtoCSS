import os
import re
from helper import protocss_dict


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

        def process_import(match):
            imported_file = match.group(1)

            if imported_file.startswith("http://") or imported_file.startswith("https://"):
                return f'@import url("{imported_file}");'
            elif imported_file.endswith(".css"):
                imported_file_path = os.path.join(f"{base_path}css/", imported_file)
                if os.path.isfile(imported_file_path):
                    return f'@import url("{imported_file_path}");'
                else:
                    return f"/* Error: File '{imported_file}' not found in static/css. */"
            elif imported_file.endswith(".ptcss"):
                imported_file_path = os.path.join(f"{base_path}/", imported_file)
                if os.path.isfile(imported_file_path):
                    # imported_file_content = read_protocss_file(imported_file_path)
                    # return imported_file_content
                    imported_file = imported_file.replace(".ptcss", ".css")
                    return f'@import url("static/css/{imported_file}");'
                else:
                    return f"/* Error: File '{imported_file}' not found in static/. */"
            elif imported_file.endswith(""):
                imported_file_path = os.path.join(f"{base_path}", f"{imported_file}.ptcss")
                if os.path.isfile(imported_file_path):
                    return f'@import url("{imported_file_path}");'
                else:
                    return f"/* Error: File '{imported_file}' not found in static/. */"
            else:
                return f"/* Error: Invalid import '{imported_file}'. */"

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
                return f"/* Group '{mixin_name}' not found. */"
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

        protocss = re.sub(r"@mq\s+([^{}]+){", expand_media_query, protocss)

        list_pattern = re.compile(r"list@(\w+)\s*:\s*\[([^\]]+)\]")

        def replace_list(match):
            list_name = match.group(1)
            list_values = [value.replace(" ", "") for value in match.group(2).split(',')]

            # Change this line to use the list name as the key in a dictionary
            self.lists[list_name] = list_values

            if list_name not in self.lists:
                return f"/* List '{list_name}' not found. */"
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
                return f"/* List '{list_name}' not found. */"

        protocss = re.sub(r"list@(\w+)\[(\d+)\]", self.replace_list_item, protocss)
        for_pattern = re.compile(r"for\s+(\w+)\s+in\s+(\w+)\s+{\s+(.[^{]+)\s+{\s+((.|\n)+?);\s+}\s+};", re.MULTILINE)

        protocss = re.sub(for_pattern, replace_for_loop, protocss)

        return protocss


def read_protocss_file(filename: str) -> str:
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return ""


def write_css_file(filename: str, css: str) -> None:
    try:
        with open(filename, "w") as f:
            f.write(css)
    except Exception as e:
        print(f"Error while writing to '{filename}': {e}")


if __name__ == '__main__':
    input_filename = "static/style.ptcss"
    fn = os.path.splitext(os.path.basename(input_filename))[0]
    output_filename = f"static/css/{fn}.css"

    protoCSS = read_protocss_file(input_filename)

    if protoCSS:
        converter = ProtoCSS()
        css = converter.convert(protoCSS)
        print(css)
        write_css_file(output_filename, css)
