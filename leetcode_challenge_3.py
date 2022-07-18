import math

test_number = 600851475143

def isPrime(number):
	print number
	if number == 1:
		return False
	for i in range(2, int(math.sqrt(number)) + 1):
		if number % i == 0:
			print(number, "isn't prime", i)
			return False
	return True


result = 0
for i in range(1, int(math.sqrt(test_number)) + 1):
	if test_number % i == 0 and isPrime(i):
		result = i

print(result)
