import testkwic
import kwic

mystr = "Hello there.\nHello there, buddy.\nHello and goodbye, buddy.\nHello is like buddy Goodbye!"
print "mystr is:\n", mystr
print testkwic.kwic(mystr, listPairs=True)
