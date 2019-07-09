from mypackage.mysubpackage2.moduleP2M1 import p2m1
from mypackage.mysubpackage1.moduleP1M1 import p1m1

import sys
print(sys.path)

if __name__ == '__main__':
    p1m1()
    p2m1()
