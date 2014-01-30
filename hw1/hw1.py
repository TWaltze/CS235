#####
# Tyler Waltze
# 1/29/14
# CS 235
# HW #1
#####

## FROM PROFESSOR ##

def forall(X, P):
	S = {x for x in X if P(x)}
	return len(S) == len(X)

def exists(X, P):
	S = {x for x in X if P(x)}
	return len(S) > 0

def subset(X,Y):
	return forall(X, lambda x: x in Y)

def all(X, P):
	return  forall(X, P)

def none(X, P):
	return  forall(X, lambda x: not P(x))

def atMostOne(X, P):
	S = {x for x in X if P(x)}
	return len(S) <= 1

def atLeastOne(X, P):
	return exists(X, P)

def prime(p):
	return  p > 1 and forall(set(range(2, p)), lambda n: p % n != 0)

def quotient(X, R):
	return {frozenset({y for y in X if (x,y) in R}) for x in X}

## WRITTEN ##

def product(A, B):
	return { (x,y) for x in A for y in B }

def isSymmetric(X, R):
	return forall(X, lambda x: forall(X, lambda y: ((x,y) in R) <= ((y,x) in R)))

def isReflexive(X, R):
	return forall(X, lambda x: (x,x) in R)

def isTransitive(X, R):
	return forall(X, lambda x: forall(X, lambda y: forall(X, lambda z: ((x,y) in R and (y,z) in R) <= ((x,z) in R))))

def isEquivalence(X, R):
	return isSymmetric(X, R) and isReflexive(X, R) and isTransitive(X, R)

def properPrimeFactors(n):
	return { x for x in set(range(2, n)) if prime(x) and n % x == 0}

def disjoint(S):
	return { (x,y) for x in S for y in S if none(properPrimeFactors(x), lambda n: n in properPrimeFactors(y)) }

def square(n):
	# set().union({1}) so when n = 1, we don't get
	# an empty set and square(1) correctly
	# returns true.
	return exists((x for x in set(range(1, n)).union({1})), lambda y: y * y == n)

def sqrt(n):
	if n == 1: return n

	for x in range(1, n):
		if x * x == n: return x
	return None

def createSquare(a, b):
	return square(a*a + b*b)

def pythagorean(S):
	return { (a,b) for a in S for b in S if createSquare(a,b) or (sqrt(b*b - a*a) in S or sqrt(a*a - b*b) in S) }

def product(S):
	product = 1
	for x in S:
		product *= x

	return product

def anotherPrimeSquare(ps):
	prod = product(ps) + 1
	for x in range(2, prod):
		if prod % x == 0 and prime(x):
			return x*x # Found prime factor, now square
	return prod * prod # No factors, must be prime itself

# 2a
X1 = {"a","b","c","d"}
R1 = {("a","a"), ("b","b"), ("c","c"), ("d","d"), ("a","b"), ("b","a"), ("c","d"), ("d","c")}

# 2b
X2 = {0,1,2,3,4,5}
R2 = {(0,0), (1,1), (2,2), (3,3), (4,4), (5,5), (0,3), (1,4), (2,5), (3,0), (4,1), (5,2)}

# 2c
X3 = set(range(-10,11))
R3 = { (x,y) for x in X3 for y in X3 if (x < 0 and y < 0) or  (x > 0 and y > 0) or x == y}

#3c
reflexive = {2, 4, 8}
symmetric = None
transitive = {8, 16, 21}

#4b
S = { x for x in set(range(1, 1200)) for y in set(range(1, 1200)) if not square(x) and createSquare(x, y) }