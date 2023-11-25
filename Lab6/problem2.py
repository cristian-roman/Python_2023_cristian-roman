import os.path
import sys


class Problem2:
    @staticmethod
    def solve():
        cnt = 1
        path = sys.argv[1]

        try:
            for file in os.listdir(path):
                if os.path.isdir(file):
                    continue
                try:
                    extension = file.split(".")[-1]
                    new_file_name = os.path.join(path, f"file{cnt}.{extension}")
                    os.rename(os.path.join(path, file), new_file_name)
                    cnt += 1
                except OSError:
                    print("Could not rename file: " + file)
        except IOError:
            print("Directory not found: " + path)
