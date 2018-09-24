import kwic

#This version verifies that the optional periodsToBreaks
#parameter worked
mystr = "zebra whale. bear apple"

assert len(kwic.kwic(mystr, periodsToBreaks=True)) == 4
