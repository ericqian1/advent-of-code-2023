input_val = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

limits = {'red': 12, 
'green': 13,
'blue': 14}

numbers = '1234567890'

sol = 0
for line in input_val.split('\n'):
	_id = line.split(':')[0][5:]
	print(_id)
	game_data = line.split(':')[1]
	draw_data = game_data.split(';')
	
	limits = {'red': 0, 
	'green': 0,
	'blue': 0}

	is_valid = True

	for draw in draw_data:
		if not is_valid:
			break

		for marb in draw.split(','):
			count = ''.join([i for i in marb if i in numbers])

			if 'red' in marb:
				color = 'red'
			if 'green' in marb:
				color = 'green'
			if 'blue' in marb:
				color = 'blue'

			if int(count) > limits[color]:
				limits[color] = int(count)

	sol += limits['red'] * limits['green'] * limits['blue']
print(sol)
