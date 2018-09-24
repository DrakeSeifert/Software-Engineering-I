import kwic7

#This version fixed the multiple words issue, optional parameters accordingly.

mystr = "hello world. This is hello"
#print kwic7.kwic(mystr, periodsToBreaks="true", ignoreWords=["test","is"])
print kwic7.kwic(mystr, periodsToBreaks="true", ignoreWords=["hello"])

