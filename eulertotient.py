def eulersTotient(n):

    r = n
    p = 2
    while p*p <=n:
	
	if n%p == 0:
	    while n%p == 0:
		n/=p

	    r *= 1- (1/float(p))
	p+=1
    if n>1:
	r *= 1 - (1/float(n))

    return r


print int(eulersTotient(189267835))