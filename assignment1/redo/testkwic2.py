import kwic

#This tests that there are no newline characters returned,
#verifying a successful linebreak
mystr = "hello world\nmy test"

assert any("\n" in s for s in kwic.kwic(mystr)[0][0]) == False

