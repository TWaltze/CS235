#####
# Tyler Waltze
# 1/29/14
# CS 235
# HW #2
#####

from fractions import gcd

# 1a

'''
7 * x + 2 = 6 (mod 31)
7 * x = 4
7 * x = 35

x = 5
'''

# 1b

'''
40 * x = 5 (mod 8)
0 * x = 5
0 = 5

No solution - Not prime/coprime
'''

# 1c

'''
3 * x + 1 = 1 (mod 3)
3 * x = 0

x = 0
'''

# 1d

'''
1 + 2 * x = 4 (mod 14)
2 * x = 3
2 * x = ... (mod 14)

No solution - Not prime/coprime
'''

# 1e

'''
17 * x + 11 = 300 (mod 389)
17 * x = 289
17 * x = 17 * 17

x = 17
'''

# 1f

'''
718581210326212034673 * x = 1 (mod 9843578223646740201)

No solution - Not prime/coprime => gcd(718581210326212034673, 9843578223646740201) == 9843578223646740201
'''

# 1g

'''
48822616 * x = 14566081015752 (mod 3333333333333333333333333)
48822616 * x = 48822616 * 298347

x = 298347
'''

# 2

def closest(t, ks):
	min = ks[0]

	for x in ks:
		if abs(t - x) < abs(t - min):
			min = x

	return min

def findCoprime(m):
	p = (3 * m // 4) + 3

	while gcd(p - 1, m) != 1:
		p = p * gcd(p - 1, m)

	return p - 1

def randByIndex(m, i):
	b = findCoprime(m)

	a = closest(4 * m // 7, [b**k for k in range(1, m.bit_length() + 1)])

	return (a * i) % m

def randInRange(minR, maxR, i):
	diff = maxR - minR

	return randByIndex(diff, i) + minR

def probablePrime(m):
	k = 20 # Number of times to run tests against m

	for i in range(2, k):
		# a must be in {2, ..., m - 1}
		a = randInRange(2, m - 1, i)

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
	n = randInRange(minR, maxR, i)

	while not probablePrime(n):
		i += 1;
		n = randInRange(minR, maxR, i)

	return n