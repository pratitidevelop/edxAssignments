# Python 3

# Be sure you have followed the instructions to download the 98-0.txt,
# the text of A Tale of Two Cities, by Charles Dickens

import collections

file = open('98-0.txt', encoding="utf8")
# print("this is the file pointer for reading file")
# print(file)
# if you want to use stopwords, here's an example of how to do this
stopwords = set(line.strip() for line in open('stopwords', encoding="utf8"))

# create your data structure here.  F
# here wordcount is a dictonary
wordcount={}

# Instantiate a dictionary, and for every word in the file, add to 
# the dictionary if it doesn't exist. If it does, increase the count.

# Hint: To eliminate duplicates, remember to split by punctuation, 
# and use case demiliters. The functions lower() and split() will be useful!

for word in file.read().lower().split():
    # print("words in flie 98-0.txt")
    # print(word)
    word = word.replace(".","")
    word = word.replace("!","")
    word = word.replace(",","")
    word = word.replace("\"","")
    word = word.replace("“","")
    if word not in stopwords:
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1

# print("after the dictonaries are made")
# print(wordcount)
# after building your wordcount, you can then sort it and return the first
# n words.  If you want, collections.Counter may be useful.

d = collections.Counter(wordcount)

print(d.most_common(10))
# for word, count in d.most_common(10):
	# print(word, ": ", count)
