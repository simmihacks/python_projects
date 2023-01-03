prev = 1
curr = 1
curr_index = 2

while len(str(curr)) < 1000:
	curr, prev, curr_index = curr + prev, curr, curr_index + 1

print curr_index