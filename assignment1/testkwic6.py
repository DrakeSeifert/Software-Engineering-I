import kwic6

#This version added periodsToBreaks.

mystr = "hello world. This is a test"
print kwic6.kwic(mystr, periodsToBreaks="true", ignoreWords=["test","is"])

