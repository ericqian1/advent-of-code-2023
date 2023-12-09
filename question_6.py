

times = [59688274]
min_dist = [543102016641022]
prod = 1

for time, dist_min in zip(times, min_dist):
	ctr = 0
	for t in range(time): 
		if t*(time-t) > dist_min:
			ctr += 1
	prod *= ctr

print(prod)