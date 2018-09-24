from copy import deepcopy

def kwic(mystr, **ignoreWords):
	if ('ignoreWords' in ignoreWords):
		#create a list of all sorted words
		sortstring = mystr.replace('\n',' ')
		sortstring = sorted(sortstring.split(' '), \
				    key=lambda x: x.lower())

		for i in ignoreWords['ignoreWords']:
			for j in sortstring:
				if i == j:
					sortstring.remove(i)
	else:
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

	#This pile of spaghetti compares each word in sortstring
	#to each word in splitword.
	#It then alters the corresponding list to read the sortstring
	#word first, followed by the rest of the words in the sentence
	#temp = []
	#for i in sortstring:
	#   for j in range(len(splitword)):
	#      temp2 = deepcopy(splitword[j])
	#      for k in range(len(splitword[j][0])):
	#         if i == splitword[j][0][k]:
	#            for y in range(len(splitword[j][0])):
	#               x = k
	#               for count in range(len(splitword[j][0])):
	#                  if x == len(splitword[j][0]):
	#                     x = 0
	#                  temp2[0][count] = splitword[j][0][x]
	#                  x = x+1
	#            temp.append(temp2)
	shift = []
	for i in sortstring:
	   for j in range(len(splitword)): #number of lines
	      temp = deepcopy(splitword[j])
	      for k in range(len(splitword[j][0])): #Number of words in a line
	         if i == splitword[j][0][k]: #This does not account for double words
	            x = k
	            for count in range(len(splitword[j][0])):
	               if x == len(splitword[j][0]):
	                  x = 0
	               temp[0][count] = splitword[j][0][x] 
	               x = x+1
                    shift.append(temp)

	#ideas to fix:
	#struct->index 0-N is sortstring, in order
	#Each word holds an int associated with how many times it occurs
	#this may actually not work -> need to sort by the next word :(
	
	finalproduct = (shift,)

	#Layers of lists and tuples:
	#finalproduct[mainTuple]
	#	     [listOfSortedStrings]
	#	     [tupleOfLinesAndLineNumber]
	#	     [listOfWords]
	#ex: 
	#finalproduct[0][0][0][0] gives "apples"
	#finalproduct[0][0][1] gives "2" etc.

	return finalproduct

#python struct equivalent:
#from collections import namedtuple
#MyStruct = namedtuple("MyStruct", "field1 field2 field3")
#m = MyStruct("foo","bar","baz") or
#m = MyStruct(field1 = "foo", field2 = "bar", field3 = "baz")

#To implement:
#ignoreWords
#listPairs
#periodsToBreaks
