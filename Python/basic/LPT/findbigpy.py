import os
import sys
import platform
import glob


def dir_walking(walkdir, min_size=1024*1024*1024):
    print(walkdir)
    for dirpath, subdirs, files in os.walk(walkdir):
        for file in files:
            fullname = os.path.join(dirpath, file)
            size = os.path.getsize(fullname)
            if size > min_size:
                print(f"({size},{fullname})")


def root_path():
    return os.path.abspath(os.sep)


if __name__ == "__main__":
    root = root_path()
    print(root)
    dir_walking(root)
