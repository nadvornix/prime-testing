

import random,gmpy,time

def nextPrime(a):
	a|=1
	i=2
	while True:
		a+=2
		if gmpy.is_prime(a):	#0=composite, 1=maybe prime 2=surely prime
			return a
		
		i+=1

gaps={}
power=20
try:
	while True:
		if power%10==0:
			print power
		start=time.time()
		p=nextPrime(2**power)
		gaps[power]=[]
		for i in range(20000):
			pnew=nextPrime(p)
			gaps[power].append(pnew-p)
			# gaps.append(pnew-p)
			# print p
			p=pnew
			if i%10==0:
				if time.time()-start > 500:
					break
		power +=5
		if power>1000:
			break

except KeyboardInterrupt:
		pass
import cPickle as pickle

f=file("gaps2.pckl","w")

pickle.dump(gaps, f)
# print gaps
# for i in gaps:
# 	f.write("%s\n"%i)
	# print i

# a=2**20+1

# b=random.randint(a,a<<1)
# print gmpy.is_prime(a+1)
# print nextPrime(a)-a