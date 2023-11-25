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
                file_path = os.path.join(path, file)
                extension = file.split(".")[-1]
                new_file_name = os.path.splitext(file_path)[0] + str(cnt) + '.' + extension
                try:
                    os.rename(file_path, new_file_name)
                    cnt += 1
                except OSError:
                    print("Could not rename file: " + file)
        except IOError:
            print("Directory not found: " + path)
