import kwic

#Tests that a list is returned. This relates to the requirements because
#we need kwic to return a list (assuming the listPairs parameter is
#not present)
mystr = ""
assert isinstance(kwic.kwic(mystr),list)
