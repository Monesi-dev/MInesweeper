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

def get_size():

	width, height = (None, None)

	while (width == None):

		print("Insert width of the grid: ")
		width = input()

		try:
			width = int(width)
			if (width <= 0):
				width = None
				print("Width must be greater than zero")
		except:
			width = None
			print("Width must be an integer")


	while (height == None):

		print("Insert height of the grid: ")
		height = input()

		try:
			height = int(height)
			if (height <= 0):
				height = None
				print("Width must be greater than zero")
		except:
			height = None
			print("Width must be an integer")

	return (width, height)

def receive_input(width, height):

	x, y = (None, None)

	while x==None:

		print("Enter x: ")
		x = input()

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
			if (y < 0 or y >= height):
				y = None
		except:
			y = None

	return (x, y)

def you_have_won():

	width = len(game_map)
	height = len(game_map[0])
	game_won = True

	for x in range(width):
		for y in range(height):
			if (map_available[x][y] == "X" and game_map[x][y] != "B"):
				game_won = False
				break

	return game_won

def reveal_all_zeros(x, y):

	global game_map, map_available
	width = len(game_map)
	height = len(game_map[0])

	if ( x >= 0 and x < width and y >= 0 and y < height): #Check if x and y are out of bound

		if (map_available[x][y] == "X"):

			map_available[x][y] = game_map[x][y]

			if (map_available[x][y] == 0):

				for dx in range(-1,2):
					for dy in range(-1,2):
						if ((dy == 0 and dx == 0) == False):
							reveal_all_zeros(x + dx,y + dy)

	return

def play():

	global game_map, map_available

	playing = True
	width, height = get_size()
	game_map = generate_map(width, height)
	map_available = [["X" for y in range(height)] for i in range(width)]

	while playing:

		display_map(map_available)
		x, y = receive_input(width, height)

        #Checks whether you have lost or not
		if (game_map[x][y] == "B"):
			playing = False
			display_map(game_map)
			print("You've lost")
		elif (game_map[x][y] == 0):
			reveal_all_zeros(x, y)
		else:
			map_available[x][y] = game_map[x][y]

		if (you_have_won()):
			playing = False
			display_map(game_map)
			print("Congratulations mate, you have won")

game_map = []
map_available = []

play()


