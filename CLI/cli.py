####################
# CLI for ProtoCSS #
####################


from colorama import Fore, Style
from CLI.cli_helper import read_version, documentation, convert, close, generate_config
from protocss import ProtoCSS


class UnknownCommandError(Exception):
    pass


class NoArgumentsError(Exception):
    pass


def print_header():
    __version__ = read_version()
    with open("ptcss_ascii.ans", "r") as file:
        contents = file.read()
        print(f"{Fore.MAGENTA}{contents}{Style.RESET_ALL}")
    print(
        f"{Fore.LIGHTWHITE_EX}ProtoCSS v{__version__}{Style.RESET_ALL} - For more information: {Fore.LIGHTCYAN_EX}https://protocss.dev{Style.RESET_ALL}\nType 'help' for general information, supported commands and more.\n")


def process_command(command):
    if command == "help":
        documentation()
    elif command == "exit" or command == "quit" or command == "close":
        close()
    elif command.startswith("convert"):
        cmd_parts = command.split(" ")
        if len(cmd_parts) > 1:
            convert(*cmd_parts[1:])
        else:
            raise NoArgumentsError("No arguments provided for 'convert' command.")
    elif command == "version":
        __version__ = read_version()
        print(f"{__version__}")
    elif command == "gconfig":
        print(f"\n{Fore.LIGHTWHITE_EX}    Generating config file...   {Style.RESET_ALL}")
        try:
            generate_config()
            print(f"{Fore.LIGHTGREEN_EX}    Configuration file generated successfully!{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.LIGHTRED_EX}Error: {str(e)}{Style.RESET_ALL}")
    else:
        raise UnknownCommandError(f"Unknown command '{command}'")


if __name__ == "__main__":
    print_header()

    while True:
        try:
            command = input(f"{Fore.LIGHTWHITE_EX}ProtoCSS >{Style.RESET_ALL} ").lower()
            process_command(command)
        except KeyboardInterrupt:
            break
        except UnknownCommandError as e:
            print(f"Error: {str(e)}")
        except NoArgumentsError as e:
            print(f"{Fore.LIGHTRED_EX}Error: {str(e)}{Style.RESET_ALL}")
