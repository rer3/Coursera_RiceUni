"""
Coursera / Rice University
Principles of Computing (Part 2)
Week 2
"""

# Reading files from the network

import urllib2
import codeskulptor

FILENAME = "examples_files_dracula.txt"

url = codeskulptor.file2url(FILENAME)
netfile = urllib2.urlopen(url)

#data = netfile.read()
#print data
#print type(data)

for line in netfile.readlines():
    print "line:", line[:-1]

## This can be done on the desktop almost identically
print url
## Cut and paste that into a web browser to get the data directly
## Copy into a file on your local machine, or use that URL on desktop
## Comment out your imports
FILENAME = "examples_files_dracula.txt"
netfile = open(FILENAME, "r")
## Everything below netfile = ... above will work just fine on desktop