import mykwic #Alex Groce's kwic
import time

file = open('30kUlysses.txt', 'r')
textFile = file.read()

print "Sorting...\n"

t0 = time.time()
mykwic.kwic(textFile, periodsToBreaks=True)
t1 = time.time()

print "\nTime elapsed: ", t1-t0
print ""
