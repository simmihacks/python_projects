import math
# can optimize by considering b must be prime for n = 0

def is_prime(number):
	if number < 2:
		return False
	for i in range(2, int(math.sqrt(number)) + 1):
		if number % i == 0:
			return False
	return True

def getSequenceLength(a, b):
	i = 0
	while True:
		calculated = i**2 + a*i + b
		if not is_prime(calculated):
			break
		i += 1
	return i

max_length = float("-inf")
max_a = 0
max_b = 0

for a in range(-999, 1000):
	print(a)
	for b in range(-1000, 1001):
		length = getSequenceLength(a, b)
		if length > max_length:
			max_length = length
			max_a, max_b = a, b

print(max_a, max_b, max_a * max_b, max_length)