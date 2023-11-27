import os
import sys


class Problem4:

    @staticmethod
    def solve():
        directory = sys.argv[1]
        dictionary = dict()
        try:
            for file in os.listdir(directory):
                try:
                    if os.path.isdir(file):
                        continue
                except IOError:
                    print("Could not read file: " + file)
                extension = file.split(".")[-1]
                dictionary[extension] = dictionary.get(extension, 0) + 1
        except IOError:
            print("Directory not found: " + directory)

        try:
            if len(dictionary) == 0:
                raise ValueError
        except ValueError:
            print("No files found.")

        for key, value in dictionary.items():
            print(f"{key}: {value}")

