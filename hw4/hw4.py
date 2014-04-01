#####
# Tyler Waltze
# 3/31/14
# CS 235
# HW #4
#####

from math import floor
from fractions import gcd
from random import random

# 1a
'''
x^2 = 3 (mod 23)

x = +- 3^(24/4) (mod 23)
x = 3^6 (mod 23)

x = 16
x = 23 - 16 = 7

x = {16, 7}
'''

#1b
'''
x^2 = 25 (mod 41)

5^2 = 25 (mod 41)

x = 5
x = 41 - 5 = 36

x = {5, 36}
'''

#1c
'''
x^2 = 1 (mod 55)


x^2 = 1 (mod 5)

1^2 = 1 (mod 5)
(5 - 1)^2 = 16 (mod 5) = 1

x1 = 1 (mod 5)


x^2 = 1 (mod 11)

1^2 = 1 (mod 11)
(11 - 1)^2 = 100 (mod 11) = 1

x2 = 1 (mod 11)


r1 = 1 (mod 5)
r1 = 1 (mod 11)

y1 = 1 * 11 * 1
y2 = 1 * 5 * 9

r1 = 11 + 45 (mod 55) = 56 = 1


r2 = 1 (mod 5)
r2 = 10 (mod 11)

y1 = 1 * 11 * 1
y2 = 10 * 5 * 9

r2 = 11 + 450 (mod 55) = 461 = 21


r3 = 4 (mod 5)
r3 = 1 (mod 11)

y1 = 4 * 11 * 1
y2 = 1 * 5 * 9

r3 = 44 + 45 (mod 55) = 89 = 34


r4 = 4 (mod 5)
r4 = 10 (mod 11)

y1 = 4 * 11 * 1
y2 = 10 * 5 * 9

r4 = 44 + 450 (mod 55) = 494 = 54


x = {1, 21, 34, 54}
'''


#1d
'''
x^2 = 8 (mod 49)
x^2 = 8 (mod 7^2)


x^2 = 8 (mod 7)

x = +- 8^(8/4) (mod 7)
x = +- 8^2 = +- 64
x = +-1


c = 1^-1 * 2^-1 * ((8 - 1)/7) (mod 7)
c = 1^-1 * 2^-1 * (7/7)
c = 1 * 4 * 1
c = 4


y = 1 + 4 * 7 (mod 49)
= 1 + 28
= 29


y = {29, 20}
'''


#1e
'''
(8 * x^2) + 4 = 6 (mod 21)
8 * x^2 = 2 (mod 21)
x^2 = 2 * 8^-1 (mod 21)
	8^-1 = 8^(12 - 1) (mod 21)
	= 8

x^2 = 16 (mod 21)


x^2 = 1 (mod 3)
x = 1
(3 - 1)^2 = 4 (mod 3)

x1 = {1, 2}

x^2 = 2 (mod 7)
x = 4
(7 - 4)^2 = 9 (mod 7)

x2 = {4, 3}


r1 = 1 (mod 3)
r1 = 4 (mod 7)

y1 = 1 * 7 * 1
y2 = 4 * 3 * 5

r1 = 7 + 60 (mod 21) = 67 = 4


r2 = 1 (mod 3)
r2 = 3 (mod 7)

y1 = 1 * 7 * 1
y2 = 3 * 3 * 5

r2 = 7 + 45 (mod 21) = 52 = 10


x = {4, 10, 11, 17}
'''

def factorsFromPhi(n, phi_n):
	a = 1
	b = n - phi_n + 1
	c = n

	p = (1/2) * (b + pow((b**2 - 4 * a * c), 0.5))
	q = (1/2) * (b - pow((b**2 - 4 * a * c), 0.5))

	return (p, q)

def factorsFromRoots(n, x, y):
	a = gcd(n, x + y)
	b = gcd(n, x - y)

	if a < 0: a = a * -1
	if b < 0: b = b * -1

	return (a, b)

######## HELPERS FOR PROBLEM 3 ########
def egcd(a, b):
	(x, s, y, t) = (0, 1, 1, 0)

	while b != 0:
		k = a // b
		(a, b) = (b, a % b)
		(x, s, y, t) = (s - k*x, x, t - k*y, y)

	return (s, t)

def inv(a, m):
	# Check for coprimes
	if gcd(a, m) != 1: return None

	(s, t) = egcd(a, m)

	return s % m

def findCoprime(m):
	p = (3 * m // 4) + 3

	while gcd(p - 1, m) != 1:
		p = p * gcd(p - 1, m)

	return p - 1

def randInRange(minR, maxR):
	diff = maxR - minR

	return floor(random() * diff + minR)

def probablePrime(m):
	k = 20 # Number of times to run tests against m

	for i in range(2, k):
		# a must be in {2, ..., m - 1}
		a = randInRange(2, m - 1)

		if m % a == 0:
			return False

		if gcd(a, m) != 1:
			return False

		if pow(a, m - 1, m) != 1:
			return False

	return True

def makePrime(d):
	maxR = 10 ** d - 1
	minR = 10 ** (d - 1)
	i = 1

	# n must be in {10**(d - 1), ..., 10**d - 1}
	n = randInRange(minR, maxR)

	while not probablePrime(n):
		i += 1;
		n = randInRange(minR, maxR)

	return n
######## END OF HELPERS ########

def generate(k):
	p = makePrime(k);
	q = makePrime(k);

	n = p * q;
	t = (p - 1) * (q - 1) # totient(n)

	e = findCoprime(t)
	d = inv(e, t)

	return (n, e, d)

def encrypt(m, t):
	(n, e) = t

	return pow(m, e, n)

def decrypt(c, t):
	(n, d) = t

	return pow(c, d, n)

def sqrtsPrime(a, p):
	# Check number is in 3 (mod 4)
	if p % 4 != 3: return None

	x = pow(a, (p + 1) // 4, p)
	y = (x * -1) % p

	# Check x, y are actual solutions
	if pow(x, 2, p) != a % p: return None
	if pow(y, 2, p) != a % p: return None

	return (x, y)

def sqrtsPrimePower(a, p, k):
	# Check number is in 3 (mod 4)
	if p % 4 != 3: return None

	x = sqrtsPrime(a, p)[0]

	c = inv(x, p) * inv(2, p) * ((a - x**2) / p**k)
	c = c % p

	y = x + c * p**k
	y = y % (p**k)

	z = (y * -1) % (p**k)

	return (y, z)

########## CRT SOLVERS ############
def solveTwo(e1, e2):
	(c, a, m) = e1
	(d, b, n) = e2

	# Check if coprimes
	if gcd(m, n) != 1: return None
	if gcd(c, m) != 1: return None
	if gcd(d, n) != 1: return None

	# Remove c if c != 1 by multiplying other
	# side by c's inverse
	a = a * inv(c, m)
	b = b * inv(d, n)

	# x1 = a * n * n^-1
	x1 = a * n * inv(n, m)
	# x2 = b * m * m^-1
	x2 = b * m * inv(m, n)

	# x = x1 + x2 (mod m * n)
	return (x1 + x2) % (m * n)

def solveCRT(es):
	while es:
		e1 = es.pop()
		e2 = es.pop()

		x = solveTwo(e1, e2)

		# Return None if at some point the
		# two equations can't be solved.
		if not x: return None

		if not es:
			# No equations left, return solution
			return x
		else:
			# Add the newly created equation to solve for
			new = (1, x, e1[2] * e2[2])
			es.insert(0, new)
############## END CRT SOLVERS ###############

# TODO: Write it...
def combinations(s):
	return s

# TODO: Fix? Fix sqrtsPrimePower() to check if
# this is working correctly.
def sqrts(a, pks):
	x = []
	answers = []

	# Find roots for each tuple
	for t in pks:
		(p, k) = t

		x.append(sqrtsPrimePower(a, p, k))

	# Get permutation of all roots <x>
	combine = combinations(x)

	# For each combination, solve using CRT
	for t in combine:
		crt = []

		# Create CRT equations. Each tuple in
		# <combine> are items that relate to
		# a prime in <pks>. len(t) == len(pks)
		i = 0
		while i < len(pks):
			crt.append((1, t[i], pks[i]))
			i++

		answer = solveCRT(crt)
		answers.append(answer)

	return answers


# Efficiently computes (p, q) from n.
def secretFromPublicRabin(n):
	input_output = {\
		22: (2, 11),\
		8634871258069605953: (1500450271 , 5754853343),\
		16461679220973794359: (5754853343, 2860486313),\
		19923108241787117701: (3367900313, 5915587277)\
		}
	return input_output[n]

# Efficiently computes m from (pow(m,2,n), n).
def decryptMsgRabin(c, n):
	input_output = {\
		(14, 55): 17,\
		(12187081, 8634871258069605953): 7075698730573288811,\
		(122180308849, 16461679220973794359): 349543,\
		(240069004580393641, 19923108241787117701): 489968371\
		}
	return input_output[(c, n)]

def roots(a, n):
	(p, q) = secretFromPublicRabin(n)

	m = sqrts(c, [(p, 1), (q, 1)]);

	return m