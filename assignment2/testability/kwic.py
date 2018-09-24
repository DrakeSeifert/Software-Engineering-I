from copy import deepcopy
from re import sub
from collections import Counter

#This version adds the listPairs parameter
def kwic(mystr, **myParameter):
	if(mystr == ""):
		emptylist = []
		return emptylist
		
	if ('periodsToBreaks' in myParameter):
		if(myParameter['periodsToBreaks'] == "true"):
			newstring = mystr.replace('\n', '')
			newstring = sub(r'(?<=[a-z])\.(?=\s)', '.\n', newstring)
			newstring = sub(r'(\n)\s', '\n', newstring)
			splitline = newstring.split('\n')
	else:
		#split string by line, returns list of sentences
		splitline = mystr.split('\n')

	#splitline = mystr.split('\n')	
	
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

	listPairShift = deepcopy(shift)

	if ('ignoreWords' in myParameter):

		for a in myParameter['ignoreWords']:
			a = a.replace(".", "")
			a = a.replace("?", "")
			a = a.replace(",", "")
			a = a.replace("!", "")
			a = a.replace(":", "")

		temp = deepcopy(shift)
		for a in myParameter['ignoreWords']:
			for i in range(len(shift)):
				count = 1
				for a in myParameter['ignoreWords']:
					#a = a.replace(".", "")
					#a = a.replace("?", "")
					#a = a.replace(",", "")
					#a = a.replace("!", "")
					#a = a.replace(":", "")
					if count == len(myParameter['ignoreWords']):
						if shift[i][0][0].lower() == a.lower():
							temp.remove(shift[i])
					else:
						count+=1
		shift = temp

	newShift = sorted(shift, key=lambda tup: (tup[0][0].lower(), \
						  tup[0][0].strip('.'), \
						  tup[0][0].strip('?'), \
						  tup[0][0].strip(','), \
						  tup[0][0].strip('!'), \
						  tup[0][0].strip(':')))
	finalproduct = (newShift)

	if ('listPairs' in myParameter):

		if(myParameter['listPairs'] == True):

			#convert shifted words to lowercase
			for i in range(len(listPairShift)):
			   for j in range(len(listPairShift[i][0])):
			      listPairShift[i][0][j] = listPairShift[i][0][j].lower()

			#remove grammar markings
			for i in range(len(listPairShift)):
			   for j in range(len(listPairShift[i][0])):
			      for k in range(len(listPairShift[i][0][j])):
			         if listPairShift[i][0][j][k] == "." or \
			            listPairShift[i][0][j][k] == "?" or \
			            listPairShift[i][0][j][k] == "," or \
			            listPairShift[i][0][j][k] == "!" or \
			            listPairShift[i][0][j][k] == ":":
			               listPairShift[i][0][j] = \
			               listPairShift[i][0][j].replace(listPairShift[i][0][j][k], "")

			myPair = {}
			findPair = Counter(elem[0][0] for elem in listPairShift)

			#find all words that appear more than once, put in dictionary
			for key, value in findPair.iteritems():
				if value > 1:
					myPair[key] = [value]

			#find what lines the words appear on, append to key's value
			for i in range(len(listPairShift)):
				for key in myPair:
				   if any(key in s for s in listPairShift[i][0]):
				      myPair[key].append(listPairShift[i][1])

			#remove the first element (the word count)
			for key in myPair:
				del myPair[key][0]

			#clean up list so each key is associated with each line
			for key in myPair:
				for i in range(len(splitword)):
					keepFirst = True
					count = myPair[key].count(i)
					while i in myPair[key]:
						if count == 1:
							break
						else:
							myPair[key].remove(i)
							count = count - 1

			#Convert dictionary to a list of tuples	
			myNewPair = myPair.items()

			#New dictionary of word pair as key, number of shared lines as value
			rekt={}
			for i in range(len(myNewPair)):
			   if i != len(myNewPair)-1:
				 if i == len(myNewPair)-2:
				    for j in myNewPair[i][1]:
				       for a in myNewPair[i+1][1]:
				          if j==a:
				             if myNewPair[i][0]+" "+myNewPair[i+1][0] in rekt.keys():
						rekt[myNewPair[i][0]+" "+myNewPair[i+1][0]]+=1
					     else:
			                     	rekt[myNewPair[i][0]+" "+myNewPair[i+1][0]]=1
			         for k in range(i+1,len(myNewPair)):
				    for j in myNewPair[i][1]:
				       for a in myNewPair[k][1]:
				          if j==a:
				             if myNewPair[i][0]+" "+myNewPair[k][0] in rekt.keys():
						rekt[myNewPair[i][0]+" "+myNewPair[k][0]]+=1
					     else:
			                     	rekt[myNewPair[i][0]+" "+myNewPair[k][0]]=1

			#convert dictionary to a list of tuples
			newRekt = rekt.items()
		
			#Remove elements for single pairs of words
			temp = deepcopy(newRekt)
			for i in range(len(newRekt)):
				if newRekt[i][1] == 1:
					del temp[i]
			newRekt = temp

			#split word pairs by whitespace
			for i in range(len(newRekt)):
				mytemp = list(newRekt[i])
				mytemp[0] = tuple(newRekt[i][0].split(' '))
				newRekt[i] = tuple(mytemp)

			#delete any doubles	
			temp = deepcopy(newRekt)
			for i in range(len(newRekt)):
				if newRekt[i][0][0] == newRekt[i][0][1]:
					del temp[i]

			newRekt = temp
	
			#Sort each pair of words
			for i in range(len(newRekt)):
				mytemp = list(newRekt[i])
				mytemp[0] = tuple(sorted(newRekt[i][0]))
				newRekt[i] = tuple(mytemp)

			newRekt = sorted(newRekt, key=lambda x:x[0])

			return (finalproduct, newRekt)

	return finalproduct
