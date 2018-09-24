from copy import deepcopy
from re import sub

def kwic(mystr, **myParameter):
	if ('periodsToBreaks' in myParameter):
		if(myParameter['periodsToBreaks'] == "true"):
			newstring = mystr.replace('\n', '')
			newstring = sub(r'(?<=[a-z])\.(?=\s)', '.\n', newstring)
			newstring = sub(r'(\n)\s', '\n', newstring)
			splitline = newstring.split('\n')
	else:
		#split string by line, returns list of sentences
		splitline = mystr.split('\n')
		

	#if ('ignoreWords' in myParameter):
	#	#create a list of all sorted words
	#	sortstring = mystr.replace('\n',' ')
	#	sortstring = sorted(sortstring.split(' '), \
	#			    key=lambda x: x.lower())

	#	for i in myParameter['ignoreWords']:
	#		for j in sortstring:
	#			if i == j:
	#				sortstring.remove(i)
	#else:
	#	#create a list of all sorted words
	#	sortstring = mystr.replace('\n',' ')
	#	sortstring = sorted(sortstring.split(' '), \
	#			    key=lambda x: x.lower())

	#split sentences by word, making splitword a list of lists
	splitword = []
	for i in range(len(splitline)):
		splitword.append(splitline[i].split(' '))

	#put each inner list into a tuple, paired with its line number
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

	if ('ignoreWords' in myParameter):
		temp = deepcopy(shift)
		for a in myParameter['ignoreWords']:
			for i in range(len(shift)):
				if shift[i][0][0] == a:
					temp.remove(shift[i])
		shift = temp

	newShift = sorted(shift, key=lambda tup:tup[0][0].lower())
	finalproduct = (newShift,)

	return finalproduct
