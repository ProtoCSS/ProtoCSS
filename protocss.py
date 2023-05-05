import re
import protocss_dict


class ProtoCSS:
    """
    The ProtoCSS class offers a powerful and streamlined solution for converting ProtoCSS code into standard CSS.
    Designed to enhance your workflow, ProtoCSS seamlessly integrates with vanilla CSS while simplifying the handling
    of variables, shorthand properties, and other unique features of the ProtoCSS language.
    """

    def __init__(self):
        self.shorthand_properties = protocss_dict.shorthand_properties

    def convert(self, protocss: str) -> str:
        # Extract and store variables
        variable_pattern = re.compile(r"@!(\w+)\s*:\s*([^;]+);")
        variables = dict(variable_pattern.findall(protocss))
        # print(variables)

        # Convert ProtoCSS variables to CSS custom properties
        css_vars = "\n".join([f"--{key}: {value};" for key, value in variables.items()])
        protocss = re.sub(variable_pattern, "", protocss)
        protocss = f":root {{\n{css_vars}\n}}\n\n" + protocss

        # Replace variable usage
        def replace_var(match):
            var_name = match.group(1)
            return f"var(--{var_name})"

        protocss = re.sub(r"%!(\w+)", replace_var, protocss)

        for shorthand, full_property in self.shorthand_properties.items():
            pattern = re.compile(rf"{shorthand}\s*:\s*(.+?);")
            protocss = pattern.sub(f"{full_property}: \\1;", protocss)

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
    input_filename = "style.prot"
    output_filename = "style.css"

    protoCSS = read_protocss_file(input_filename)

    if protoCSS:
        converter = ProtoCSS()
        css = converter.convert(protoCSS)
        print(css)
        # write_css_file(output_filename, css)
