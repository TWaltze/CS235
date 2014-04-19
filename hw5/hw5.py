#####
# Tyler Waltze
# 4/16/14
# CS 235
# HW #5
#####

from math import floor
from fractions import gcd
from random import randint
from urllib.request import urlopen

# 1a
'''
[1,2,3,0] o [3,0,1,2]

[1,2,3,0] [3,0,1,2] = [0,x,x,x]
[1,2,3,0] [3,0,1,2] = [0,1,x,x]
[1,2,3,0] [3,0,1,2] = [0,1,2,x]
[1,2,3,0] [3,0,1,2] = [0,1,2,3]

Solution: [0, 1, 2, 3]
'''

# 1b
'''
[46,47,...,99,0,1,2,3,4,...,45] o [11,12,...,99,0,1,2,3,4,...,10]

46 + 11 (mod 100) = 57

Solution: [57, 58, ..., 99, 0, 1, 2, ..., 56]
'''

# 1c
'''
p o q o p^-1 o q^-1

p o q o p^-1 o q^-1 = p o p^-1 o q o q^-1

p o p^-1 = C_n
q o q^-1 = C_n

C_n = [0, 1, 2, ..., n - 1]

C_n o C_n = [0, 1, 2, ..., n - 1]

Solution: [0, 1, 2, ..., n - 1]
'''

# 1d
'''
p o p o p o p

Solution: p
'''

# 1e
'''
[0,1] => 1
[1,0] => 3

(S_2, o):

[0,1] o [0,1] = [0,1]
[0,1] o [1,0] = [1,0]
[1,0] o [0,1] = [1,0]
[1,0] o [1,0] = [0,1]

((Z/4Z)*, *):

1 * 1 = 1
1 * 3 = 3
3 * 1 = 3
3 * 3 = 1
'''

# 1f
'''
'''

# 1g
'''
2 => 1
4 => 2
8 => 3
1 => 0
'''

# 1h
'''
There is no isomorphism because they are sets of two different sizes (4 vs 5).
'''

# 2a
def permute(p, l):
	new = []

	for x in p:
		new.append(l[x]);

	return new

# 2b
def C(k, m):
	return [(x + k) % m for x in range(0, m)]

# 2c
def M(a, m):
	return [(x * a) % m for x in range(0, m)]

# 2d
def isSorted(l):
	check = list(l)
	check.sort()

	return l == check

def sort(l):
	length = len(l)

	if isSorted(l):
		return [x for x in range(0, length)]

	for x in range(1, length):
		# Test each cyclic permutation to see
		# if it ever sorts
		p = C(x, length)
		cyclic = permute(p, l)

		if isSorted(cyclic): return p

		# Test each multiplication permutation
		p = M(x, length)
		mult = permute(p, l)

		if isSorted(mult): return p

	return None

# 3a
def unreliableUntrustedProduct(xs, n):
	url = 'http://cs-people.bu.edu/lapets/235/unreliable.php'
	return int(urlopen(url+"?n="+str(n)+"&data="+",".join([str(x) for x in xs])).read().decode())

def prod(xs, p):
	result = 1

	for x in xs:
		result = (result * x) % p

	return result

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

def encrypt(m, public_key):
	(n, e) = public_key

	return pow(m, e, n)

def decrypt(c, private_key):
	(n, d) = private_key

	return pow(c, d, n)

def privateProducts(xs, p, q):
	encrypted = []

	# Generate phi(p * q)
	phi = (p - 1) * (q - 1)
	n = p * q
	e = findCoprime(phi)

	'''
	e = 2

	# Find e | {2, ..., phi - 1} && gcd(e, phi) = 1
	while e < phi and gcd(e, phi) != 1:
		e += 1
	'''

	public_key = (n, e)

	# RSA encrpyt all xs values
	for x in xs:
		encrypted.append(encrypt(x, public_key))

	encryptedProd = unreliableUntrustedProduct(encrypted, n)

	d = inv(e, phi)
	decryptedProd = decrypt(encryptedProd, (n, d))

	return decryptedProd % p

# 3b
def validPrivateProducts(xs, p, q):
	isomorphism = []
	r = randint(2, q)

	for x in xs:
		c = (x * q * inv(q, p) + r * p * inv(p, q)) % (p * q)

		isomorphism.append(c)

	product = privateProducts(isomorphism, p, q)
	check = privateProducts(isomorphism, q, p)

	# Check that we have a valid product.
	# r^len(xs) == sum(xs) % q
	if pow(r, len(xs), q) == check:
		return product
	else:
		return validPrivateProducts(isomorphism, p, q)