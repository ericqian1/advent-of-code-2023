input_txt = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""


tot_score = 0
cards = {}
counts = {}
for i, line in enumerate(input_txt.split('\n')):
	# PARSE
	data = line.split(':')[1]
	winning = data.split('|')[0]
	yours = data.split('|')[1]
	w_no = winning.split(' ')
	y_no = yours.split(' ')
	# CLEAN UP A BIT
	w_no = [i for i in w_no if i != '']
	y_no = [i for i in y_no if i != '']

	counters = {}
	cards[i] = 0 
	counts[i] = 1
	for no in w_no:
		counters[no] = 0
	
	for no in y_no:
		if no in w_no:
			cards[i] += 1

for i in range(len(counts)):
	for j in range(counts[i]):
		for k in range(cards[i]):
			counts[k+i+1] += 1
 
print(sum([v for k,v in counts.items()]))