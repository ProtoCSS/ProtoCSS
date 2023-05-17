import os
import re
import time
import sys
from colorama import Fore, Style
from CLI.helper import *

__version__ = read_version()

print(
    f"{Fore.LIGHTWHITE_EX}ProtoCSS v{__version__}{Style.RESET_ALL} - For more information: {Fore.LIGHTCYAN_EX}https://protocss.dev{Style.RESET_ALL}\nType 'docs' for general information, supported commands and more.\n")

while True:
    try:
        command = input(f"{Fore.LIGHTWHITE_EX}ProtoCSS >{Style.RESET_ALL} ")

        if command == "docs":
            documentation()
        elif command == "exit" or command == "quit" or command == "close":
            close()
        elif command.startswith("convert"):
            cmd_parts = command.split(" ")
            if len(cmd_parts) > 1:
                convert(*cmd_parts[1:])
            else:
                print("Error: No arguments provided for 'convert' command.")
        elif command == "version":
            print(f"{__version__}")
        else:
            print(f"Error: Unknown command '{command}'")
    except KeyboardInterrupt:
        break
