from kwic0 import *

#This test makes sure that the kwic function returns a tuple
mystr = "Hello world, this is a test!"
assert isinstance(kwic(mystr), tuple)
