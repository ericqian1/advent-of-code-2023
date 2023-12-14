input_txt = """.....................................................................................#......#...............................................
..#.....#.................................................................#........................#........................................
...............................#...............................................................................#.....#......................
.................................................#.............#...............................#...................................#........
..............#......#.................#...............#............#.............#..........................................#..............
.........................................................................................#.................#...............................#
.#..........................................................................................................................................
..........................#......#............................................#......#.................................#....................
.................................................................................................#..........................................
.........................................#..........#..........#............................................................#...............
......#.....#......#..........................#........................#....................................................................
....................................#.........................................................................#..........................#..
..................................................................................#.........................................................
...................................................................................................................#........................
.................................................................#........................................#.................................
.............................#..............................#..........................#.......#............................................
..........................................#.....#.............................#.............................................................
#..................#..................................................................................................................#.....
....................................#...................#..........................#...........................#..............#.............
........#................#...................#.............................................................................................#
...............................#....................#...........................................#...........................................
.......................................#..............................................#.....................................................
........................................................................#........#...........................#..............................
..................................#........#...................#........................................#.........#.................#.......
#................#........................................................................................................#.................
.........#.......................................#...............................................#.............................#........#...
...............................................................................................................#............................
.........................................................................................#..................................................
...........................................................#..................................#..........#...........................#......
......#.........................#..........................................................................................#................
....................#.....................#.......#...............................#.................................#.......................
..........................#..............................................#..................................................................
..........#..........................#.......................#...................................#..............#..............#...........#
......................................................#.....................................................................................
............................................................................................................................................
#...............................................#................#............................#.............................................
..................#......................#............................#................................#................................#...
............................................................................................................................................
....................................................#....................................#.............................#....................
..............#...................#................................#..........#..............................#.............................#
............................#...............................................................................................#...............
....#.................#.....................................#..........#............................................................#.......
......................................................#.....................................................................................
...........#..............................#.................................................#..........#.................#..................
.................................#..............#................#..........#.......#.......................................................
...................................................................................................................#..............#.........
#...........................................................................................................#...............................
........#.......#............................................................................................................#..............
............................#.....................#..........#......................................#.....................................#.
.....................................#.................................................#........................#...........................
.........................................................................................................................#...........#......
.......................#.............................#........................#.............................................................
..............#...............................#.................#..................#........#...............................................
...#......................................................................#.................................#..............................#
...................#..................#.............................................................................#........#..............
............................................................................................................................................
.........................#.........................#........................................................................................
......#......#.............................................#.............................#............#.....................................
.................................#......................................#...................................................................
.........................................#........................#..............................#.................#..............#.........
............................................................................................................................................
......................................................#.................................................#..............#..................#.
......................#......#...............#...................................#............................#.............................
....#...........#.................#............................................................#...............................#............
..........................................................................#..........................#......................................
..........................................#................................................#...............................#............#...
................................................................................................................#...........................
..........#....................................#...................................................................................#........
................................#....................#..............................................................#.......................
......#.......................................................#...............................#.............................................
#.......................#.....................................................................................................#.............
.................#...................#...........................................#..........................#...............................
.....................................................................#....................#.................................................
..............................#.................#.......#.........................................#.........................................
..#........................................................................#....................................#.........#.................
...........#............................#..........................................#.............................................#..........
......#.............................................................................................................#.....................#.
........................................................................................................#...................................
..............#...................#.........#...............................................................................................
........................................................#.............#..........#.....#..........#............................#............
.........#......................................................#...........................#...............................................
.........................................#...................................#.................................#............................
............................................................................................................................................
................#...................................................................#.................#..................#..................
.................................#..........................#.............#....................#................................#..........#
...#........................#.........................................................................................................#.....
.................................................#......................................#.....................#......#......................
...........................................#.........................#........#.............................................................
........#......#...................................................................................................................#.....#..
.#..................#..................................#.........#..........................................................................
..................................#.....#.................................#.................................................................
...................................................#.................................#......................................................
............................................................#...............................................................................
.............................................#......................#..........#............#.........................#......#..............
................................#...................................................................#.......................................
.....................................................#..................#......................................#............................
...#......................#.....................................................................................................#...........
...........#...........................................................................#..............................................#.....
................#..................................................#..............................................#.........................
.......................#......................................................................#.............................................
................................#........#.........#.....................#.....#......................#.....................................
.#..........................................................................................................................................
........................................................#................................#...................#..................#...........
.....................................#........#.................................................#.......................................#...
.........#...........#......................................................................................................................
....................................................#.............................................................#.................#.......
.............#............#........................................#.............#.....................#...................#...............#
..................#....................#.................................#.............#....................................................
................................................#...........................................................................................
.......................#...............................................................................................#....................
....#..........................................................#.....#..............#...........................................#...........
...............................................................................................#..................#.......................#.
.........#...................#............................................#.................................................................
.............................................................................................................#..............#......#........
...........................................................................................#................................................
.#...........................................................#..............................................................................
..............#..............................#........................................#.............#.......................................
....................................#..............#..............#.........#.............................#.............#.............#.....
....................#............................................................................................#..........................
.........................................................................................#..................................................
...........#............................#................#....................................................................#.............
.....#......................................................................................................#...............................
..................................#................................................#........#.............................................#.
.#................#......#...........................................................................#......................................
..............................................#.......................#................#............................................#.......
.........#............................#........................#..........................................#.....#......#....................
..............................................................................................#.............................................
........................................................................................................................................#...
..........................#........................#...............#................................#............................#..........
..#........................................#............#............................................................#......................
...............................#.....#........................................#.......#......................................#..............
.......................................................................................................#....................................
.....................................................#..............................................................................#.......
........#......................................#...........................#.............................................#.................#
...................#.....#......................................#.............................#.............................................
............#.........................#......................................................................#.......#.................#....
..............................#...................................................#.........................................................
............................................#.........................................................#.....................................
.......#..........................#................#.....#.............#....................................................................
..................#.........................................................#.............#.......................................#........."""


lines = input_txt.split('\n')
galaxies = []


for x, line in enumerate(lines):
	for y, char in enumerate(line):
		if char=='#':
			galaxies.append((x,y))

x_doubles = []
y_doubles = []
x_galaxies = [i[0] for i in galaxies]
y_galaxies = [i[1] for i in galaxies]

print(x_galaxies)
for x, line in enumerate(lines):
	if x not in x_galaxies:
		x_doubles.append(x)

for y, line in enumerate(lines[0]):
	if y not in y_galaxies:
		y_doubles.append(y)

from itertools import combinations

print(x_doubles, y_doubles)
a = combinations(galaxies, 2) 

ctr = 0
for g_1, g_2 in a:
	x_1, y_1 = g_1 
	x_2, y_2 = g_2 

	sorted_x = sorted([x_1, x_2])
	for x in range(sorted_x[0], sorted_x[1]):
		if x in x_doubles:
			ctr += 1000000
		else:
			ctr += 1

	sorted_y = sorted([y_1, y_2])
	for y in range(sorted_y[0], sorted_y[1]):
		if y in y_doubles:
			ctr += 1000000
		else:
			ctr += 1	

print(ctr)		