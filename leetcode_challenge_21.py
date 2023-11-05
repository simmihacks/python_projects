import math
import itertools

max_num = 1000

sieve = [0] * max_num

primes = []

for i in range(2, max_num):
	if sieve[i] == 0:
		primes.append(i)
		j = i 
		while j < max_num:
			sieve[j] = 1
			j += i

def sum_divisors(num):
	total_sum = 0
	for i in range(1, int(math.sqrt(num)) + 1):
		if num % i == 0:
			if i == math.sqrt(num):
				total_sum += i
			else:
				total_sum += i + num / i
	return total_sum - num

def sum_divisors_smart(num):
	divisors = 1
	factorization_primes = []
	factorization_exponents = []
	for prime in primes:
		if prime > num:
			break
		curr_num = num
		exponent = 0
		while curr_num % prime == 0:
			curr_num /= prime
			exponent += 1
		divisors *= exponent + 1
		if exponent > 0:
			factorization_primes.append(prime)
			factorization_exponents.append(exponent)
	total = 0
	exponent_ranges = [range(n + 1) for n in factorization_exponents]
	for combo in itertools.product(*exponent_ranges):
		product = 1
		for i, combo_factor in enumerate(combo):
			product *= factorization_primes[i]**combo_factor
		total += product
	return total - num





def naive_sum():
	amicables = set()
	for a in range(1, max_num):
		# print(a)
		if a in amicables:
			continue
		for b in range(a + 1, max_num):
			if sum_divisors(a) == b and sum_divisors(b) == a:
				print("found", a, b)
				amicables.add(a)
				amicables.add(b)
	print(sum(amicables))

naive_sum()

def smart_sum():
	amicables = set()

	for a in range(1, max_num):
		# print a
		if a in amicables:
			continue
		for b in range(a + 1, max_num):
			if sum_divisors_smart(a) == b and sum_divisors_smart(b) == a:
				print("found", a, b)
				amicables.add(a)
				amicables.add(b)
	print(sum(amicables))

# smart_sum()
