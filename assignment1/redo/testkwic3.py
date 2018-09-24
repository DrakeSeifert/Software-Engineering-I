import kwic

#This version verifies there is no whitespace returned,
#showing I successfully split each line by word.
mystr = "hello world\nmy test"

assert any(" " in s for s in kwic.kwic(mystr)[0][0]) == False
