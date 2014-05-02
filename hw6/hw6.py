#####
# Tyler Waltze
# 5/1/14
# CS 235
# HW #6
#####

from math import floor
from fractions import gcd
from random import randint

# 1a
'''
12 * x = 16 (mod 32)

gcd(12, 32) = 4

3 * x = 4 (mod 8)

3^-1 (mod 8) = 3

x = 12 (mod 8)
x = 4 (mod 8)

Solution: x = 4 (mod 8)
'''

# 1b
'''
x = 7 (mod 21)
x = 21 (mod 49)

gcd(21, 49) = 7

7 (mod 7) = 0
21 (mod 7) = 0

z = x/7 = 1 (mod 3)
z = x/7 = 3 (mod 7)

x = 1 (mod 3)
x = 3 (mod 7)

3^-1 (mod 7) = 5
7^-1 (mod 3) = 1

z = (1 * 7 * 1) + (3 * 3 * 5)
z = 7 + 45
z = 52

52 = x / 7
x = 52 * 7 (mod 147) = 364 = 70 (mod 147)

Solution: x = 70 (mod 147)
'''

# 1c
'''
2 * x = 12 (mod 26)

gcd(2, 26) = 2

x = 6 (mod 13)

Solution: x = 6 (mod 13)
'''

# 1d
'''
x = 11 (mod 14)
x = 18 (mod 21)

gcd(14, 21) = 7

11 (mod 7) = 4
18 (mod 7) = 4

(x - 4) / 7 = 7 / 7 (mod 2)
(x - 4) / 7 = 14 / 7 (mod 3)

z = (x - 4) / 7 = 1 (mod 2)
z = (x - 4) / 7 = 2 (mod 3)

x = 1 (mod 2)
x = 2 (mod 3)

z = 5 (mod 6)

5 = (x - 4) / 7
35 = x - 4
x = 39 (mod 42)

Solution: x = 39 (mod 42)
'''

# 1e
'''
x = 10 (mod 12)
x = 2 (mod 16)

gcd(12, 16) = 4

10 (mod 4) = 2
2 (mod 4) = 2

z = (x - 2) / 4 = 8 / 4 (mod 3)
z = (x - 2) / 4 = 0 / 4 (mod 4)

z = 2 (mod 3)
z = 0 (mod 4)

z = 8 (mod 12)

8 = (x - 2) / 4
32 = x - 2
x = 34 (mod 48)

Solution: x = 34 (mod 48)
'''

# 1f
'''
x^2 = 4 (mod 35)
3 * x = 15 (mod 21)


x^2 = 4 (mod 35)

x^2 = 4 (mod 5)
x^2 = 4 (mod 7)

y = 4 (mod 5)
y = 4 (mod 7)

x = 2 (mod 35)
x = 33 (mod 35)
x = 12 (mod 35)
x = 23 (mod 35)


3 * x = 15 (mod 21)

gcd(3, 21) = 3

x = 5 (mod 7)


x = 2 (mod 35)
x = 33 (mod 35)
x = 12 (mod 35)
x = 23 (mod 35)
x = 5 (mod 7)

gcd(35, 7) = 7

2 (mod 7) = 2
33 (mod 7) = 5
12 (mod 7) = 5
23 (mod 7) = 2
5 (mod 7) = 5

r = 5

x = 33 (mod 35)
x = 12 (mod 35)
x = 5 (mod 7)

z = (x - 5) / 7 = 7 / 7 (mod 5)
z = (x - 5) / 7 = 5 / 7 (mod 1)

Solution: No solution.
'''

# 2a
'''
16 * x - 2 = 6 (mod 12)
16 * x = 8 (mod 12)

gcd(16, 12) = 4

4 * x = 2 (mod 3)
x = 2 (mod 3)

16 * 2 - 2 = 30

Solution: It is currently 6am, and the alarm rang 30hrs ago.
'''

# 2b
'''
x = y (mod 2^8)
x = z (mod 2^4)

gcd(2^4, 2^8) = 16

x = y (mod 16)
x = z (mod 1)

Solution: 16 different passwords
'''

# 2c
'''
x = 1 (mod 12)
x = 7 (mod 15)

gcd(12, 15) = 3

1 (mod 3) = 1
7 (mod 3) = 1

z = (x - 1) / 3 = 0 (mod 4)
z = (x - 1) / 3 = 2 (mod 5)

z = 0 (mod 4)
z = 2 (mod 5)

z = 2 * 4 * 4^1
z = 32 (mod 20) = 12 (mod 20)

12 = (x - 1) / 3
36 = x - 1
x = 37

Solution: Bob has 37 problems. Because 37 is prime,
there is no number of single-capacity machines that can
all be used to full capacity (ignoring capacity of 1).
'''

# 3a, 3b, 3c
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

def linearCongruence(c, a, m):
	g = gcd(c, m)

	# If gcd > 1 and it doesn't divide a,
	# there is no solution
	if a % g != 0: return None

	c = c // g
	a = a // g
	m = m // g

	return (c, a, m)

def basicCRT(e1, e2):
	(c, a, m) = e1
	(d, b, n) = e2

	# Check if coprimes
	if gcd(m, n) != 1: return None
	if gcd(c, m) != 1: return None
	if gcd(d, n) != 1: return None

	mod = m * n
	x = ((a * n * inv(n, m)) + (b * m * inv(m, n))) % mod

	return (x, mod)

def generalCRT(e1, e2):
	(c, a, m) = e1
	(d, b, n) = e2

	g = gcd(m, n)

	# Find remainder value. If they
	# aren't equal, no solution.
	if a % g == b % g:
		r = a % g
	else:
		return None

	# Start general CRT
	a = (a - r) // g
	b = (b - r) // g
	mg = m // g
	ng = n // g

	z = ((a * ng * inv(ng, mg)) + (b * mg * inv(mg, ng))) % (mg * ng)

	mod = (m * n) // g
	x = ((z * g) + r) % mod

	return (x, mod)

def solveOne(c, a, m):
	(c, a, m) = linearCongruence(c, a, m)

	return (a * inv(c, m)) % m

def solveSystem(e1, e2):
	(c, a, m) = e1
	(d, b, n) = e2

	# Run linear congruence on each equation
	e1 = linearCongruence(c, a, m)
	e2 = linearCongruence(d, b, n)

	# Pass along possible error
	if e1 == None or e2 == None: return None

	(c, a, m) = e1
	(d, b, n) = e2

	# Solve each equation to get basic
	# form x = y (mod n)
	a = solveOne(c, a, m)
	b = solveOne(d, b, n)

	# If one of the above (e1, e2) can't be solved,
	# the system can't be solved.
	if a == None or b == None: return None

	# If gcd(a, b) == 1, solve with basic CRT
	if gcd(a, b) == 1:
		return basicCRT((c, a, m), (d, b, n))
	else:
		return generalCRT((c, a, m), (d, b, n))

def solveTwo(e1, e2):
	answer = solveSystem(e1, e2)

	if answer == None: return None
	else: return answer[0]

def solveAll(es):
	while es:
		e1 = es.pop()
		e2 = es.pop()

		answer = solveSystem(e1, e2)

		# Return None if at some point the
		# two equations can't be solved.
		if not answer: return None

		if not es:
			# No equations left, return solution
			return answer[0]
		else:
			# Add the newly created equation to solve for
			new = (1, answer[0], answer[1])
			es.insert(0, new)