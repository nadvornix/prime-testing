
import random
import time
import gmpy

def is_prime_rm(n,s): #n,s prir., n>3 a liche
    '''
    return (rounds, res):
    - rounds is -1 if it passed all tests (ie: probably prime)
    '''
    r = n - 1; u = 0
    while r % 2 == 0:
        r >>= 1; u += 1
    # mame n-1 = (2**u)*r, kde r je liche
    for i in xrange(0, s): # 0,1,...,s-1
        a = random.randint(2,n-2) #nah. c. mezi 2 a n-2
        z = pow(a,r,n) #modularni mocneni
        if z != 1 and z != n-1:
            for j in xrange(0,u): #0,1,...,u-1
                # z = z*z % n
                z = pow(z,2,n)
                if z == 1: return (i, 0) #je slozene
                if z == n-1: break
            else:
                return (i, 0) #je slozene
    return (-1, 1) #proslo testem

lens=[]
try:
    for i in range(5,2000000):
        if i%10000==0:
            print i
        start=time.time()
        rounds, res = is_prime_rm(i,100)
        lens.append( (i,rounds,gmpy.is_prime(i,100)))

except KeyboardInterrupt:
        pass

import cPickle as pickle
f=file("rmM.pckl","w")
pickle.dump(lens, f)