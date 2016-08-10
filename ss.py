import random,gmpy,time



def is_prime_ss(n,s): #n,s prirozena, n>3 liche
	'''
	return (rounds, res):
	- rounds is -1 if it passed all tests (ie: probably prime)
	'''
	for i in xrange(0, s): # 0,1,...,s-1
		a = random.randint(2,n-2) #nah. c. mezi 2 a n-2

		if gmpy.gcd(a,n) != 1:
			return (i, 0) #je slozene

		p = pow(a,(n-1)/2,n)
		if p == n-1: 
			p = -1

		if not gmpy.jacobi(a,n) == p:
			return (i, 0) #je slozene
	    
	return (-1, 1) #n proslo testem

# for i in range(5,30):
# 	print i,is_prime_ss(i,10)


lens=[]
try:
    for i in range(5,2000000):
        if i%10000==0:
            print i
        start=time.time()
        rounds, res = is_prime_ss(i,100)
        lens.append( (i,rounds,gmpy.is_prime(i,100)))

except KeyboardInterrupt:
        pass

import cPickle as pickle
f=file("ssM.pckl","w")

pickle.dump(lens, f)
