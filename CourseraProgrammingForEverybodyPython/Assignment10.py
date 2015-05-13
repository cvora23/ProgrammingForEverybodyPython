'''
Created on May 11, 2015

@author: cvora

10.2 Write a program to read through the mbox-short.txt and figure out the 
distribution by hour of the day for each of the messages. You can pull the 
hour out from the 'From ' line by finding the time and then splitting the 
string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, 
sorted by hour as shown below. Note that the autograder does not have 
support for the sorted() function.

'''
fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
timingList = dict()

fh = open(fname)
count = 0
for line in fh:
    if not line.startswith("From"): continue
    words = line.split()
    if (words[0] == "From"):
        timings = words[5].split(':')
        timingList[int(timings[0])] = timingList.get(int(timings[0]),0) + 1

timings = timingList.items()
timings.sort
for k,v in timings:
    print '%02d' % k + ' ' + str(v)