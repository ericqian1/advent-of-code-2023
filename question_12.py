from itertools import combinations

input_txt = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""


def check(tot_vals, input_str):

	tot_count = 0 
	tot_arr = [int(i) for i in tot_vals]
	tot_sum = sum(tot_arr)
	qs = [i for i in input_str if i=='?']
	q_idxs = [i for i, j in enumerate(input_str) if j=='?']
	idx_map = {i:j for i,j in enumerate(q_idxs)}
	vals = [i for i in input_str if i=='#']
	alloc = tot_sum - len(vals)
	idxs = [i for i in range(tot_sum)]

	for i in combinations(q_idxs, alloc):
		arr_str = list(input_str)
		other_idxs = [j for j in q_idxs if j not in i]

		for j in other_idxs:
			arr_str[j] = '.'

		for j in i:
			arr_str[j] = '#'

		ctrs = []
		new_ctr = 0
		for i, j in enumerate(arr_str):
			if j=='#':
				new_ctr += 1
			else:
				if new_ctr > 0:
					ctrs.append(new_ctr)
					new_ctr = 0 
			if i == len(arr_str) - 1:
				if new_ctr > 0: 
					ctrs.append(new_ctr)

		valid_combo = True

		for i,j in zip(ctrs, tot_vals):
			if i!=int(j):
				valid_combo = False
		if valid_combo:
			tot_count += 1 

	return tot_count	


lines = input_txt.split('\n')
tot_count = 0

for line in lines:
	input_str, n_so = line.split(' ')
	tot_vals = n_so.split(',')
	if input_str[0] == '.':
		ct_1 = check(tot_vals, input_str)
		ct_2 = check(tot_vals, '?' + input_str)
		val_1 = ct_2**(4) * ct_1
	else:
		ct_1 = check(tot_vals, input_str)
		ct_2 = check(tot_vals, input_str + '?')
		val_1 =  ct_2**(4) * ct_1

	tot_count += val_1

print(tot_count)