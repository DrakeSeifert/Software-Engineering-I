import kwic5

#This version added the ignoreWords parameter.

#mystr = "ZHello world,\nthis is a test!\napples and oranges\nbears are scary"
mystr = "hello world\nthis is a test"
print kwic5.kwic(mystr)
print kwic5.kwic(mystr, ignoreWords=["test","is"])

