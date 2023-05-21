import os
import re
import sys
from colorama import Back, Fore, Style
from helper.errors import ProtoCSSError
from protocss import ProtoCSS, read_protocss_file, write_css_file
from glob import glob

converter = ProtoCSS()


def icon_ans():
    with open("ptcss_icon.ans", "r") as file:
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
    # clear the screen
    print("\033[H\033[J") if sys.platform.startswith('linux') or sys.platform.startswith('darwin') else os.system('cls')
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

ProtoCSS is a superset of CSS that offers a streamlined solution for writing style sheets. 
It enhances the traditional functionality of CSS, blending in the manageability of variables, shorthand properties, 
reusable style mixins, loops and conditions from other paradigms. 

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
    converter = ProtoCSS()

    def process_file(file_path, output_path=None):
        try:
            protoCSS = read_protocss_file(file_path)
            if protoCSS:
                css = converter.convert(protoCSS)
                if css is not None:
                    if output_path is None:
                        output_path = os.path.dirname(file_path)
                    fn = os.path.splitext(os.path.basename(file_path))[0]
                    output_filename = os.path.join(output_path, f"{fn}.css")
                    write_css_file(output_filename, css)
                    print(
                        f"\n\t{Back.BLUE}{Fore.LIGHTWHITE_EX}\t{fn}.ptcss converted successfully to {output_filename}\t{Style.RESET_ALL}\n")
                else:
                    print(f"\n {Fore.RED}Conversion failed for {file_path}\n\n")
            else:
                print(f"\n\t{Back.WHITE}{Fore.LIGHTWHITE_EX}\tNothing to convert in {file_path}\t{Style.RESET_ALL}\n")
        except ProtoCSSError as e:
            print(f" {Fore.RED}{e}")

# File-Path is working properly
    if args[0] in ("-f", "--file"):
        file_path = args[1]
        output_path = None
        if "-o" in args:
            output_index = args.index("-o") + 1
            if output_index < len(args):
                output_path = args[output_index]
                print(output_path)
        process_file(file_path, output_path)

# TODO: Multi-File-Path is working properly, but tries to read the "-o" as a file path.
    elif args[0] in ("-mf", "--multi-file"):
        file_paths = args[1:]
        output_path = None
        if "-o" in args:
            output_index = args.index("-o") + 1
            if output_index < len(args):
                output_path = args[output_index]
                print(output_path)
        for file_path in file_paths:
            process_file(file_path, output_path)

# Dir-Path is working properly
    elif args[0] in ("-d", "--dir"):
        dir_path = args[1]
        output_path = None
        if "-o" in args:
            output_index = args.index("-o") + 1
            if output_index < len(args):
                output_path = args[output_index]
                print(output_path)
        for file_path in glob(os.path.join(dir_path, '*.ptcss')):
            process_file(file_path, output_path)

    # File-Default is working properly
    elif args[0] in ("-fd", "--file-def", "-mfd", "--multi-file-def"):
        file_paths = args[1:]
        for file_path in file_paths:
            process_file(file_path)

    # Dir-Default is working properly
    elif args[0] in ("-dd", "--dir-def"):
        dir_path = args[1]
        for file_path in glob(os.path.join(dir_path, '*.ptcss')):
            process_file(file_path)

    elif args[0] in ("-h", "--help"):
        print("""
    Usage: convert [options] [file|dir]

    Options:
        -f, --file: Converts a ProtoCSS file to CSS, to a chosen directory.
        -mf, --multi-file: Converts multiple ProtoCSS files to CSS, to a chosen directory.
        -d, --dir: Converts all ProtoCSS files in a directory to CSS, to a chosen directory.
        -h, --help: Displays this section.

    Default:
        -fd, --file-def: Converts a ProtoCSS file to CSS, to the same directory.
        -mfd, --multi-file-def: Converts multiple ProtoCSS files to CSS, to the same directory.
        -dd, --dir-def: Converts all ProtoCSS files in a directory to CSS, to the same directory.

            """)
    else:
        print("Error: Unknown argument")
