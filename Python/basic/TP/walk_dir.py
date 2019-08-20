import os
import sys
from pathlib import Path, PurePath


def walk(dirname="."):
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)
        try:
            if os.path.isfile(path):
                print(path)
            else:
                walk(path)
        except Exception as e:
            print(f"{e} : {path}")


if __name__ == "__main__":
    home = Path.home()
    root = PurePath(home).anchor
    print(f"home: {home} \nroot: {root}")
    print(sys.path)
    print(os.getenv('PYTHONPATH'))
