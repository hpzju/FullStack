print("enter mypackage")

from .mysubpackage1 import *
from .mysubpackage2 import *


__all__ = mysubpackage1.__all__ + mysubpackage2.__all__


print("exit mypackage")