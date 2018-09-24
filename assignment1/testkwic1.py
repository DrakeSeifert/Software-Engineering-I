from kwic1 import *

#This test makes sure that the kwic function returns two inputs in the first element
mystr = "zHello world,\nthis is a test!"
print kwic(mystr)
assert len(kwic(mystr)) == 2 #FIXME this is too specific and can pass later tests
