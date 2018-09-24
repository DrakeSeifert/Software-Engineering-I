import kwic

#This version verifies that the listPairs parameter works
#mystr="hello there.\nhello THERE, buddy.\nhello ANd goodbye buddy.\nhello IS like buddy goodbye!"

#assert len(kwic.kwic(mystr, listPairs=True)[1]) == 4

mystr = "Design is hard\nLet's just implement"

print kwic.kwic(mystr, ignoreWords=["hard."])
