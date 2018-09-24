from kwic import Kwic

mystr = "Hello world. This is the test. Wowza holy shmokes"


kc = Kwic(periodsToBreaks=True, ignoreWords=["the"])
i1 = kc.index()
print "TEST: kc.index() constructor returns:\n",i1
kc.addText(mystr)
i1 = kc.index()
print "TEST: kc.index() returns:\n",i1
kc.addText(" here is more hello text world. World zebra hello apples")
i2 = kc.index()
print "TEST: i1 is:\n",i1
print "TEST: i2 is:\n",i2
p1 = kc.listPairs()
print "TEST: p1 is:\n",p1
kc.reset()
i3 = kc.index()
print "TEST: i3 is:\n",i3
kc.addText("New text")
i3 = kc.index()
print "TEST: i3 is:\n",i3
kc.printLog()
