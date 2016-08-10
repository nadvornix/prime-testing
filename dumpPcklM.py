

import cPickle as pickle
import sys

a=pickle.load(file(sys.argv[1]))

for i,rounds, p in a:
	if i%2==1:
		if p==1:
			p==2
		print "%s,%s,%s"%(i,rounds,p)