def randomize(seed,seed2=3.9023812482388931):
    return seed2 * seed * (1-seed)

def random(times,seed2=3.9023812482388931):
	b = 0.500000000001
	for a in range(times):
		b = randomize(b,seed2)
		print(int(str(b)[10]),end='')

