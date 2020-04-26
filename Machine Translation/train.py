import sys

# This looks good 
bigrams = {} # This is going to be your matrix for the counts (not bigrams, but word coocurrences)
vocabulary1 = [] # Vocabulary in language 1
vocabulary2 = [] # Vocabulary in language 2
file1 = open(sys.argv[1]) # This is language 1 input file
file2 = open(sys.argv[2]) # This is language 2 input file


# Loop through each line in file 1, put the value of the line in the variable "line"
# for line in file1:
while True:
	s1 = file1.readline() # read a line from file 1 into the variable "s1" 
	s2 = file2.readline() # read a line from file 2 into the variable "s2"
# if the lines are empty it has reached the end of the file(s)
	if s1 == '':
		break
	vocabulary1 += s1.strip('\n').split(' ') # Add the tokens in line 1 to the vocab of lang 1
	vocabulary2 += s2.strip('\n').split(' ')

# Here we have created the vocabulary, we close the files

file1.close()
file2.close()

# This will unique the vocabularies (lists may have more than one element that is identical)
vocabulary1 = list(set(vocabulary1))
vocabulary2 = list(set(vocabulary2))

# Initialise the cooccurrence matrix
for tok1 in vocabulary1: # For each token in the vocab ulary of language 1
	for tok2 in vocabulary2: # For each token in the vocab of language 2
		if tok1 not in bigrams:
			bigrams[tok1] = {}
	if tok2 not in bigrams[tok1]:
		bigrams[tok1][tok2] = 0

# Now we have an initialised matrix where for each pair of tokens the value is 0

# Now we need to collect the counts.

file1 = open(sys.argv[1]) # This is language 1 input file
file2 = open(sys.argv[2]) # This is language 2 input file

while True:
	s1 = file1.readline() # read a line from file 1 into the variable "s1"
	s2 = file2.readline() # read a line from file 2 into the variable "s2"
# if the lines are empty it has reached the end of the file(s)
	if s1 == '':
		break
# Tokenise the input lines
	tokens1 = s1.strip('\n').split(' ')
	tokens2 = s2.strip('\n').split(' ')

	for tok1 in tokens1:
		for tok2 in tokens2:
			try:
				bigrams[tok1][tok2] += 1
			except:
				bigrams[tok1][tok2] = 1
for word1 in bigrams:
	for word2 in bigrams[word1]:
		print(bigrams[word1][word2] / len( bigrams[word1] ))
		print(word1 + " " + word2)
