def kwic(mystr):
	splitline = (mystr.lower()).split('\n') #split string by line, returns list
	splitword = [splitline[0].split(' '), splitline[1].split(' ')] #split by words
	mylist = sorted(splitword) #FIXME Sort by index in next version?
	return tuple(mylist)
