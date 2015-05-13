'''
Created on May 11, 2015

@author: cvora

7.2 Write a program that prompts for a file name, then opens that file and 
reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the 
lines and compute the average of those values and produce an output as shown below.

'''
# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
doubleArray = list()
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    words = line.split()
    doubleArray.append(float(words[1]))
print "Average spam confidence: " + str(float((sum(doubleArray))/(len(doubleArray)))) 

