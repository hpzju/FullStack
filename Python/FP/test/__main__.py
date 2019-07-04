import sys
import os

if __name__ == "__main__":
    print(sys.path)
    print(f"{sys.executable}")
    print(f"pwd: {os.getcwd()}")
    dirname, filename = os.path.split(os.path.abspath(__file__))
    print(f"dirname: {dirname}, filename: {filename}")
    fpPath = os.path.abspath(os.path.join(dirname, os.pardir))
    print(f"FP path: {fpPath}")
    if fpPath not in sys.path:
        sys.path.append(fpPath)
    print(sys.path)
