import kwic

#This version verifies the line shifts now sort properly
mystr = "zebra whale\nbear apple"

assert kwic.kwic(mystr)[0][0][0] == "apple"
