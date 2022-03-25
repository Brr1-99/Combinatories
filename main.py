import math
import itertools

posibilities = math.factorial(10)

comb = itertools.permutations(range(1,11),10)

result = [x for x in comb]

def get_loop_length(tuple):
	return 0