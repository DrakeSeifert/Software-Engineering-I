import kwic2

#This tests that the tuple returned has one more element than the number of newlines within the string
mystr = "ZHello world,\nthis is a test!\napples and oranges\nbears are scary"
print kwic2.kwic(mystr)
print mystr.count('\n')
print len(kwic2.kwic(mystr))
assert mystr.count('\n') == len(kwic2.kwic(mystr)) - 1
#FIXME assert too specific? -> it may work if next test I introduce the line number
