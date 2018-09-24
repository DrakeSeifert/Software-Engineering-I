#I added the ability to split each line into words
def kwic(mystr):

	#split string by line, returns list of sentences
	splitline = mystr.split('\n')

	#split sentences by word, making splitword a list of lists
        splitword = []
        for i in range(len(splitline)):
		splitword.append(splitline[i].split(' '))


	endResult = ([(splitword[0],0)])

	return endResult
