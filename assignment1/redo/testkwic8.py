import kwic

#This tests the ignoreWords parameter works properly
mystr = "zebra whale\nbear apple"

assert kwic.kwic(mystr, ignoreWords=["apple"])[0][0][0] == "bear"
