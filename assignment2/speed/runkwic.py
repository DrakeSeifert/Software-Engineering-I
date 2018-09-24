import kwic
import fastkwic
import time

#mystr = "Hello world\nThis is a test\nBananas are tasty"
#print "\nmystr is:\n", mystr

file = open('100Ulysses.txt', 'r')
textFile = file.read()

print "Sorting...\n"

t0 = time.time()
fastkwic.kwic(textFile, periodsToBreaks=True)
#fastkwic.kwic(mystr)
t1 = time.time()

print "\nTime elapsed: ", t1-t0
print ""

#BASE Alex Groce's kwic 30k lines: 718.207
#BASE Alex Groce's kwic 5k lines: 62.923
#BASE Alex Groce's kwic 1k lines: 8.629

#BASE kwic 30k lines: 291.253
#BASE kwic 5k lines: 47.709, 44.638, 42.544 -- AVG: 44.964
#BASE kwic 1k lines: 7.830, 7.586, 7.686 -- AVG: 7.701

#fastkwic tests:
#range to xrange 1k: 7.600, 6.802, 7.531 -- AVG: 7.311
#range to xrange 30k: 293.847 :(
 


#3 lines:
#Base: 0.00079 
#fastkwic1: 0.17713 
#fastkwic2: 0.00203 

#100 lines:
#Base: 0.035 
#fastkwic1: 0.040
#fastkwic2: 0.027 

#250 lines:
#Base: 0.111 
#fastkwic1: 0.121
#fastkwic2: 0.084

#500 lines:
#Base: 0.238
#fastkwic1: 0.255
#fastkwic2: 0.179

#1000 lines
#Base: 0.473 
#fastkwic1: 0.543
#fastkwic2: 0.380

#2000 lines
#Base: 0.995 
#fastkwic1: 1.045 
#fastkwic2: 0.862

#5000 lines
#Base: 2.848
#fastkwic1: 3.056 
#fastkwic2: 2.908

#30,000 lines
#Base: 18.710
#fastkwic1: 20.042
#fastkwic2: 20.315
