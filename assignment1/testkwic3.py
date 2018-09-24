import kwic3

#This test makes sure the last value in the inner list is an int. This int is the line number of its corresponding string.
mystr = "ZHello world,\nthis is a test!\napples and oranges\nbears are scary"
assert isinstance(kwic3.kwic(mystr)[0][(len(kwic3.kwic(mystr)[0]) - 1)], int)
