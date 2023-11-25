import os
import sys


class Problem_1:
    @staticmethod
    def solve():
        path = sys.argv[0]
        file_extension = sys.argv[1]

        file_extension = file_extension.lower()

        try:
            for file in os.listdir(path):
                file = os.path.join(path, file)
                if file.endswith(file_extension):
                    try:
                        with open(file, "r") as f:
                            print(f.read())
                    except IOError:
                        print("Could not read file: " + file)
        except FileNotFoundError:
            print("Directory not found: " + path)
