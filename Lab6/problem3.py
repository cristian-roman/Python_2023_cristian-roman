import os
import sys


class Problem3:

    @staticmethod
    def solve():
        path = sys.argv[1]
        total_size = 0
        number_of_files = 0
        try:
            for file in os.listdir(path):
                if os.path.isdir(file):
                    continue
                try:
                    size = os.path.getsize(file)
                    total_size += size
                    number_of_files += 1
                except OSError:
                    print("Could not get size of file: " + file)
        except IOError:
            print("Directory not found: " + path)

        print(f"Total size: {total_size} bytes")