
import random, gmpy,time
def is_prime_fermat(n,s): #n,s prirozena
	'1=prime, 0=sloz'
	for i in xrange(s):
		a = random.randint(2,n-2) #zvol nahodne cele cislo mezi 2 a n-2 vcetne
		print a,gmpy.gcd(a,n), pow(a,n-1,n)
		if gmpy.gcd(a,n) != 1:
			return (i, 0) #je slozene

		if pow(a,n-1,n) != 1: #pouzijeme modularni mocneni
			return (i, 0) #je slozene

	return (-1, 1) #proslo testem


lens=[]
try:
    for i in range(5,2000000):
        if i%10000==0:
            print i
        start=time.time()
        rounds, res = is_prime_fermat(i,100)
        print i, rounds, res
        lens.append( (i,rounds, gmpy.is_prime(i,100)) )

except KeyboardInterrupt:
        pass

# import cPickle as pickle
# f=file("fermatM.pckl","w")
# pickle.dump(lens, f)
