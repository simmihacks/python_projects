import math

prime_count = 0


def isPrime(number):
	print number
	if number == 1:
		return False
	for i in range(2, int(math.sqrt(number)) + 1):
		if number % i == 0:
			print(number, "isn't prime", i)
			return False
	return True

curr = 1
while prime_count < 10001:
	curr += 1
	if isPrime(curr):
		prime_count += 1

print curr
