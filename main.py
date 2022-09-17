import random

def generate_map(width, height):

	# Generate the map 
	my_map = [[0 for y in range(height)] for x in range(width)]

	#Randomly place bombs in the map
	num_bombs = width*height//5
	bombs_placed = 0

	while bombs_placed < num_bombs :

		x = random.randint(0, width - 1)
		y = random.randint(0, height - 1)

		if (my_map[x][y] != "B"):
			bombs_placed += 1
			my_map[x][y] = "B"

	#Write the number in each cell corresponding to the number of bombs that sorround the cell
	for x in range(width):
		for y in range(height):
			if (my_map[x][y] != "B"):
				for dx in range(-1,2):
					for dy in range(-1,2):

						x_to_check = x + dx
						y_to_check = y + dy

						#I am checking if the cell I am checking is on the map or not
						if(y_to_check >= 0 and y_to_check < height and x_to_check >= 0 and x_to_check < width):
							if(my_map[x_to_check][y_to_check] == "B"):
								my_map[x][y] += 1

	return my_map

def display_map(map_to_display):

	height = len(map_to_display[0])
	width = len(map_to_display)

	for y in range(height):

		row = []
		for x in range(width):
			cell = map_to_display[x][y]
			row.append(str(cell))

		print(" ".join(row))

def play(width, height):

	playing = True
	game_map = generate_map(width, height)
	map_available = [["X" for y in range(height)] for i in range(width)]

	while playing:

		display_map(map_available)
		x, y = (None, None)

		while x==None:

			#Select the value of x
			print("Enter x: ")
			x = input()

			#Validating Input
			try:
				x = int(x)
				if (x < 0 or x >= width):
					x = None
			except:
				x = None

		while y==None:

			#Receiving the value of y
			print("Enter y: ")
			y = input()

			#Validating Input
			try:
				y = int(y)
				if (y < 0 or y >= width):
					y = None
			except:
				y = None

        #Checks whether you have lost or not
		if (game_map[x][y] == "B"):
			playing = False
			display_map(game_map)
			print("You've lost")
		else:
			map_available[x][y] = game_map[x][y]

play(10,10)


