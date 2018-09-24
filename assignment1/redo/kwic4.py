#This version appends the lines corresponding line number
#to the end of the tuple
def kwic(mystr):

	#split string by line, returns list of sentences
	splitline = mystr.split('\n')

	#split sentences by word, making splitword a list of lists
        splitword = []
        for i in range(len(splitline)):
		splitword.append(splitline[i].split(' '))

	t = ()
	for i in range(len(splitword)):
		splitword[i] = t + (splitword[i], i)

	endResult = (splitword)

	return endResult
