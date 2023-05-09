import os
import re
from helper import protocss_dict


class ProtoCSS:

    def __init__(self):
        self.shorthand_properties = protocss_dict.shorthand_properties

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
            elif imported_file.endswith(".prt"):
                imported_file_path = os.path.join(f"{base_path}/", imported_file)
                if os.path.isfile(imported_file_path):
                    # imported_file_content = read_protocss_file(imported_file_path)
                    # return imported_file_content
                    imported_file = imported_file.replace(".prt", ".css")
                    return f'@import url("static/css/{imported_file}");'
                else:
                    return f"/* Error: File '{imported_file}' not found in static/. */"
            elif imported_file.endswith(""):
                imported_file_path = os.path.join(f"{base_path}", f"{imported_file}.prt")
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
        group_pattern = re.compile(r"group@(\w+)\s*\{([^}]+)\}")
        groups = {}
        for match in group_pattern.findall(protocss):
            group_name = match[0]
            group_styles = match[1]
            groups[group_name] = group_styles.strip()

        def replace_group(match):
            group_name = match.group(1)
            if group_name not in groups:
                return f"/* Group '{group_name}' not found. */"
            group_styles = groups[group_name]
            # Expand shorthand properties within the group
            for shorthand, full_property in self.shorthand_properties.items():
                pattern = re.compile(rf"{shorthand}\s*:\s*(.+?);")
                group_styles = pattern.sub(f"{full_property}: \\1;", group_styles)
            return group_styles

        protocss = re.sub(r"group@(\w+);", replace_group, protocss)
        protocss = re.sub(group_pattern, "", protocss)  # Remove group declarations

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
    input_filename = "static/style.prt"
    fn = os.path.splitext(os.path.basename(input_filename))[0]
    output_filename = f"static/css/{fn}.css"

    protoCSS = read_protocss_file(input_filename)

    if protoCSS:
        converter = ProtoCSS()
        css = converter.convert(protoCSS)
        print(css)
        write_css_file(output_filename, css)
