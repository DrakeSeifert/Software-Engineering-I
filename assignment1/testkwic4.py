import kwic4

#This version sorts everything alphabetically and shifts the string.
#Everything from here on out will be additional parameters

#assert checks if the number of inner tuples is equal to the number of words in the string
mystr = "ZHello world,\nthis is a test!\napples and oranges\nbears are scary"
print kwic4.kwic(mystr)

assert len(kwic4.kwic(mystr)[0]) == len(sorted((mystr.replace('\n',' ').split(' '))))
