

import cPickle as pickle
import sys
print sys.argv[1]

a=pickle.load(file(sys.argv[1]))

for k,v in a.items():
	print "{",k,", {"
	print ", ".join(map(str,v)),
	print "}\n}"