import kwic

#this is testing for kwic to return something that isn't empty
mystr = "hello world\nmy test"
expectedLen = len(filter(lambda c:c == "\n", mystr))
assert len(kwic.kwic(mystr)) >= expectedLen
