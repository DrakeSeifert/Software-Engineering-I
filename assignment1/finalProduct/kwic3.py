def kwic(mystr):
	splitline = mystr.split('\n')

	#split sentences by word, making splitword a list of lists
	splitword = []
	for i in range(len(splitline)):
		splitword.append(splitline[i].split(' '))

	return splitword
