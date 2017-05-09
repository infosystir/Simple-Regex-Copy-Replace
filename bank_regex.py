import re
from sys import argv

# This part means you have to run scrip.py filename1 filename2 from the command line

script, filename1, filename2 = argv

#Opens filename2 as read-write and assigns it a value of g

g = open (filename2, "r+")

print "Let's read the file %r!" % filename2

#Opens filename1, assigns it f
#loops through each line in f
#takes whatever is in the () and adds a comma afterwards
#writes each line it reads/writes to filename2

with open(filename1) as f:
    for line in f.readlines():
        output = re.sub('(\d\d\/\d\d)', r'\1,', line)
        g.write(output)
