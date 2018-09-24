import copy
def kwic(mystr):
	#create a list of all sorted words
	sortstring = mystr.replace('\n',' ')
	sortstring = sorted(sortstring.split(' '), \
			    key=lambda x: x.lower())

	#split string by line, returns list of sentences
	splitline = mystr.split('\n')

	#split sentences by word, making splitword a list of lists
	splitword = []
	for i in range(len(splitline)):
		splitword.append(splitline[i].split(' '))

	#put each inner list into a tuple, paired with its line number
	t = ()
	for i in range(len(splitword)):
		splitword[i] = t + (splitword[i], i)

	#This spaghetti code compares each word in sortstring
	#to each word in splitword.
	#It then alters the corresponding list to read the sortstring
	#word first, followed by the rest of the words in the sentence
	temp = []
	for i in sortstring:
	   for j in range(len(splitword)):
	      temp2 = copy.deepcopy(splitword[j])
	      for k in range(len(splitword[j][0])):
	         if i == splitword[j][0][k]:
	            for y in range(len(splitword[j][0])):
	               x = k
	               for count in range(len(splitword[j][0])):
	                  if x == len(splitword[j][0]):
	                     x = 0
	                  temp2[0][count] = splitword[j][0][x]
	                  x = x+1
	            temp.append(temp2)
	
	finalproduct = (temp,)

	#Layers of lists and tuples:
	#finalproduct[mainTuple]
	#	     [listOfSortedStrings]
	#	     [tupleOfLinesAndLineNumber]
	#	     [listOfWords]
	#ex: 
	#finalproduct[0][0][0][0] gives "apples"
	#finalproduct[0][0][1] gives "2" etc.

	return finalproduct
