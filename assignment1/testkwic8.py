import kwic8

#This version fixed the multiple words issue, optional parameters accordingly.

mystr = "hello world. This is hello asdf"
#print kwic7.kwic(mystr, periodsToBreaks="true", ignoreWords=["test","is"])
print kwic8.kwic(mystr, periodsToBreaks="true", ignoreWords=["hello"], listPairs="true")

