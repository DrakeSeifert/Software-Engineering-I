import kwic

#This version verifies that there are four tuples created,
#one for each line shift.
mystr = "zebra whale\nbear apple"

assert len(kwic.kwic(mystr)) == 4
