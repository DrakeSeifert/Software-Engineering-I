import kwic

#This tests that I got the line number appended to the tuple
mystr = "hello world\nmy test"

assert kwic.kwic(mystr)[1][1] == 1
