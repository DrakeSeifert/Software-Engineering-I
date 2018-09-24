import kwic


mystr = "hello\nworld"
#assert(kwic0.kwic(mystr) == [])
#assert(kwic1.kwic(mystr) == [mystr])
assert(len(kwic.kwic(mystr))==2)
