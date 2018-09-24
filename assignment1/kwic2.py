def kwic(mystr):
	splitline = mystr.split('\n') #split string by line, returns list
	splitword = []
	for i in range(len(splitline)):
		splitword.append(splitline[i].split(' '))
	mylist = sorted(splitword, key=lambda x: x[0].lower())
	return tuple(mylist)
