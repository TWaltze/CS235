#####
# Tyler Waltze
# 2/23/14
# CS 235
# HW #3
#####

from math import floor
from fractions import gcd

# 1a

'''
8 * x = 2 (mod 5)
8 * 8^(5-2) * x = 2 * 8^(5-2)
x = 2 * 8^3
x = 1024

Solution: x = 4
'''

# 1b

'''
x = 1 (mod 7)
x = 3 (mod 5)


x = 1 (mod 7)
x = 0 (mod 5)

x = 5 * y

5 * y = 1 (mod 7)
y = 1 * 5^5
y = 3

x = 5 * 3 (mod 35)
x = 15


x = 0 (mod 7)
x = 3 (mod 5)

x = 7 * y

7 * y = 3 (mod 5)
y = 3 * 7^3
y = 4

x = 7 * 4 (mod 35)
x = 28


x = 15 + 28 (mod 35)
x = 43

Solution: x = 8
'''

# 1c

'''
x = 2 (mod p)
x = 4 (mod q)

x1 = a * q * q^-1 (mod (p * q))
= 2 * q * 3
= 6 * q

x2 = b * p * p^-1 (mod (p * q))
= 4 * p * 5
= 20 * p

Solution: x = 6 * q + 20 * p (mod (p * q))
'''

# 1d

'''
x = 3 (mod 5)
x = 6 (mod 14)


x = 3 (mod 5)
x = 0 (mod 14)

x = 14 * y

14 * y = 3 (mod 5)
y = 3 * 14^3
y = 3 * 4
y = 2

x = 14 * 2 (mod 70)
x = 28


x = 0 (mod 5)
x = 6 (mod 14)

x = 5 * y

5 * y = 6 (mod 14)
y = 6 * 5^-1

	5^-1 = 5^(t(14) - 1)

		t(14) = t(7) * t(2)
		= (7 - 1) * (2 - 1)
		= 6 * 1
		= 6

	5^-1 = 5^(6 - 1)
	= 5^5 (mod 14)
	= 3

y = 18
= 4

x = 5 * 4 (mod 70)
x = 20


x = 28 + 20 (mod 70)

Solution: x = 48
'''


# PROFESSOR'S CODE
def egcd(a, b):
	(x, s, y, t) = (0, 1, 1, 0)

	while b != 0:
		k = a // b
		(a, b) = (b, a % b)
		(x, s, y, t) = (s - k*x, x, t - k*y, y)

	return (s, t)

# 2a
def invPrime(a, p):
	if a == 0: return None

	return pow(a, p - 2, p)

# 2b
def inv(a, m):
	# Check for coprimes
	if gcd(a, m) != 1: return None

	(s, t) = egcd(a, m)

	return s % m

# 3a
def solveOne(c, a, m):
	# Check if coprime
	if gcd(c, m) != 1: return None

	return (a * inv(c, m)) % m

# 3b
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

# 3c
def solveAll(es):
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

# 4a
def sumOfPowers(nes, ps):
	es = []

	# Get an equation or each prime
	for prime in ps:
		total = 0

		# Sum all powers mod each prime
		for number in nes:
			base = number[0]
			power = number[1]

			total = total + pow(base, power, prime)

		# Treat sum as new x value to use as an equation
		es.append((1, total, prime))

	return solveAll(es)
