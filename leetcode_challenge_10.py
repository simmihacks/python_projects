max_num = 2000000

sieve = [0] * max_num

primes_sum = 0

for i in range(2, max_num):
	if sieve[i] == 0:
		primes_sum += i
		j = i 
		while j < max_num:
			sieve[j] = 1
			j += i

print(primes_sum)
