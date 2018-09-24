# The from..import statement

from math import sqrt
print("Square root of 16 is", sqrt(16))

# A module's __name__

import module_using_name

# Making Your Own Modules

import mymodule

mymodule.say_hi()
print('Version', mymodule.__version__)

#---

from mymodule import say_hi, __version__

say_hi()
print('Version', __version__)

# The dir function

import sys

print(dir(sys))

print(dir())

a = 5

print(dir())

del a

print(dir())
