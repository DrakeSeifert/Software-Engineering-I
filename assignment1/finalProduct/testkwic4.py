import kwic


mystr = "hello world. my test. apples oranges"
#asseirt(kwic0.kwic(mystr) == [])
#assert(kwic1.kwic(mystr) == [mystr])
#assert(len(kwic3.kwic(mystr))==2)
#assert len(kwic3.kwic(mystr)) == 3
assert kwic.kwic(mystr, periodsToBreaks="true", ignoreWords=["hello"])[0][0][0][0] == "apples"
