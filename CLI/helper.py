import re
import sys


def icon_ans():
    with open("./CLI/ptcss_icon.ans", "r") as file:
        contents = file.read()
        return contents
def read_version():
    try:
        with open("./helper/.env", "r") as file:
            contents = file.read()
            version_match = re.search(r"VERSION=(\d+)\.(\d+)\.(\d+)-(.+)", contents)
            __version__ = version_match.group(0).split("=")[1]
            return __version__
    except Exception as e:
        print(f"Failed to read version from .env file due to error: {e}")
        return "unknown"

def close():
    sys.exit(0)

def documentation():
    docs_general = """
            -------------------------GENERAL------------------------
            
            - docs: Displays this documentation.
            - exit, quit, close: Closes the CLI.
            - convert: Converts a ProtoCSS file to CSS.
            - version: Displays the current version of ProtoCSS.
            - help: Displays this documentation.
            - clear, cls: Clears the screen.
        """

    docs = docs_general

    print("""Welcome to ProtoCSS's docs!

ProtoCSS is a robust superset of CSS that offers a streamlined solution for writing style sheets. 
It enhances the traditional functionality of CSS, blending in the manageability of variables, shorthand properties, 
reusable style mixins, and conditions from other paradigms. 

The docs is still under development, so please be patient :)\n""")

    def read_line_gen(s):
        for line in s.split('\n'):
            yield line.strip()

    while True:
        command = input("docs > ")
        match command:
            case 'general':
                for line in read_line_gen(docs_general):
                    print(line)
            case 'full':
                for line in read_line_gen(docs):
                    print(line)
            case 'quit':
                break
            case _:
                print(f"Error: Unknown command '{command}'")


def convert(*args, **kwargs):
    # print(f"Converting {' '.join(args)}")
    # for key, value in kwargs.items():
    #     print(f"{key}: {value}")

    if args[0] == "-f" or args[0] == "--file":
        print(f"Converting file {' '.join(args[1:])}")
    elif args[0] == "-d" or args[0] == "--dir":
        print(f"Converting dir {' '.join(args[1:])}")
    elif args[0] == "-mf" or args[0] == "--multi-file":
        print(f"Converting multiple files {' '.join(args[1:])}")
    elif args[0] == "-fd":
        print(f"Converting file {' '.join(args[1:])}")
    elif args[0] == "-dd":
        print(f"Converting dir {' '.join(args[1:])}")
    elif args[0] == "-mfd":
        print(f"Converting multiple files {' '.join(args[1:])}")
    elif args[0] == "-h" or args[0] == "--help":
        print("""
        Usage: convert [options] [file|dir]
        
        Options:
            -f, --file: Converts a ProtoCSS file to CSS, to a chosen directory.
            -mf, --multi-file: Converts multiple ProtoCSS files to CSS, to a chosen directory.
            -d, --dir: Converts all ProtoCSS files in a directory to CSS, to a chosen directory.
            -h, --help: Displays this section.
        
        Default:
            -fd: Converts a ProtoCSS file in the current directory to CSS, to the current directory.
            -mfd: Converts multiple ProtoCSS files in the current directory to CSS, to the current directory.
            -dd: Converts all ProtoCSS files in the current directory to CSS, to the current directory.
        """)
    else:
        print("Error: Unknown argument")