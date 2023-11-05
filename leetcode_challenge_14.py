longest_chain = float("-inf")
longest_chain_starter = -1

def getChainLength(num):
	length = 1
	while num != 1:
		if num % 2 == 0:
			num /= 2
		else:
			num = 3 * num + 1
		length += 1
	return length

for i in range(1, 1000000):
	chain_length = getChainLength(i)
	# print(i, chain_length)
	if chain_length > longest_chain:
		longest_chain, longest_chain_starter = chain_length, i
print(longest_chain_starter)
