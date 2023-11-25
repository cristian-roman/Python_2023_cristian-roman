import os
import sys


class Problem1:
    class ExtensionNotFoundException(Exception):
        def __init__(self, extension: str):
            super().__init__(f"Extension {extension} not found.")

    @staticmethod
    def solve():
        path = sys.argv[1]
        file_extension = sys.argv[2]

        file_extension = file_extension.lower()

        try:
            for file in os.listdir(path):
                if os.path.isdir(file):
                    continue
                try:
                    if file.endswith(file_extension):
                        try:
                            with open(file, "r") as f:
                                print("File: " + file)
                                print(f.read())
                        except IOError:
                            print("Could not read file: " + file)
                    else:
                        raise Problem1.ExtensionNotFoundException(file_extension)
                except Problem1.ExtensionNotFoundException:
                    print(f"For file {file} extension {file_extension} is not valid.")
        except IOError:
            print("Directory not found: " + path)
