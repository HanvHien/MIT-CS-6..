def genPrimes():
	''' Have the generator keep a list of the primes it's generated. 
	A candidate number x is prime if (x % p) != 0 for all earlier primes p. ''' 

	x = 3

	for i in xrange(2,x):
		print i 

		if (x % i) != 0: 
			retval = x
	x += 1		
	yield retval

pr = genPrimes()
for i in xrange(10):
	pr.next()
