#Each shift is now properly sorted, everything added from here on out
#will be related to optional parameters
from copy import deepcopy

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

	shift = []
        for i in range(len(splitword)):
                temp = deepcopy(splitword[i])
                for j in range(len(temp[0])):
                        x = j
                        for k in range(len(temp[0])):
                                temp[0][k] = splitword[i][0][x]
                                x = x+1
                                if x == len(temp[0]):
                                        x = 0
                        temp2 = deepcopy(temp)
                        shift.append(temp2)

	newShift = sorted(shift, key=lambda tup:tup[0][0].lower())

	endResult = (newShift)

	return endResult
