'''
Created on May 11, 2015

@author: cvora

9.4 Write a program to read through the mbox-short.txt and 
figure out who has the sent the greatest number of mail messages. 
The program looks for 'From ' lines and takes the second word of 
those lines as the person who sent the mail. The program creates a 
Python dictionary that maps the sender's mail address to a count of 
the number of times they appear in the file. After the dictionary is 
produced, the program reads through the dictionary using a maximum loop 
to find the most prolific committer.

'''
fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
emailAddrList = dict()

fh = open(fname)
count = 0
for line in fh:
    if not line.startswith("From"): continue
    words = line.split()
    if(words[0] == "From"):
        emailAddrList[words[1]] = emailAddrList.get(words[1],0) + 1

maxEmailsFrom = ''
maxEmailCount = 0
for key in emailAddrList:
    if(emailAddrList[key] >= maxEmailCount):
        maxEmailCount = emailAddrList[key]
        maxEmailsFrom = key

print maxEmailsFrom + ' '+ str(maxEmailCount)

    