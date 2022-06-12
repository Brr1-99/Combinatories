import math
import itertools


def loop_idx(arr, idx):
	# Given a value of the array it searchs for the size of the loop
	# The loop ends if the value is equal to the index
	# Or if we loop through a repeated index
    steps = 0
    memo_idxs = []
    # Main loop
    while True:
        val = arr[idx]
        steps += 1
        if idx == val:
            return steps
        if idx in memo_idxs:
            return steps - 1
        memo_idxs.append(idx)
        idx = val


def fun(arr):
	# Loop for the elements of each posibilitiy
	# Check each index for the greatest loop
	# If it's bigger than half the length of the array, it is a bad scenario
    for idx,val in enumerate(arr):
        steps = loop_idx(arr, idx)
        if steps > len(arr)/2:
            return 1
    return 0


def main(n):
	# Calculate all total cases: both number and permutations physically
	result = 0
	posibilities = math.factorial(n)
	comb = itertools.permutations(range(n),n)
	for x in comb:
		result += fun(x)
	# Computate percentage of failure cases
	percentage = (1-(result/posibilities))*100
	total = format(percentage, '.2f')
	print(f'The percentage of surviving is: {total} % \n{posibilities-result} favorable cases out of {posibilities} total cases.')

main(10)