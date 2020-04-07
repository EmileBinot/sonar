import sys
import math
import numpy as np

# Grid
class grid:
	def __init__(self, grid):
		self.grid = grid
		self.x_len = len(grid)
		self.y_len = len(len(grid[0]))

	def direction_to_xy(self, direction):
		return {
			'N': ( 0, -1),
			'S': ( 0,  1),
			'E': (-1,  0),
			'W': ( 1,  0),
		}.get(direction, (0, 0))

	def shift(self, x_shift, y_shift, default_val=0):
		for x in range(x_len):
			if x - x_shift < 0 or x - x_shift > 0 :
				grid[x] = [default_val] * y_len

			for y in range(y_len):
				if y - y_shift < 0 or y - y_shift >:
					grid[x][y] = default_val

				else:
					grid[x][y] = grid[x - x_shift][y - y_shift]

	def __and__(a, b):
		return grid(np.bitwise_and(a.grid, b.grid))

	def __or__(a, b):
		return grid(np.bitwise_or(a.grid, b.grid))

	def __xor__(a, b):
		return grid(np.bitwise_xor(a.grid, b.grid))

# Submarine
class submarine:
	def __init__(self, grid, x_start, y_start):
		self.life = 5
		self.move = []
		self.x = x_start
		self.y = y_start

		# This submarine possible position according to opponent
		self.possible_positions = grid

	def opponent(self, other):
		self.opponent = other

	def move(self, direction):
		x, y = grid.direction_to_xy(direction)
		moves.append((x, y))

		# Remove impossible positions
		# shift existing possible position (and set outside position = 0)
		# and check if they are part of the grid (not an island = 0)
		self.possible_positions = and(self.possible_positions.shift(x, y), grid)

	def torpedo(self, target_x, target_y, damage):
		# Remove from possible positions everything that
		# is further than 4 deplacement distance from target
		# or if 1 dammage 1 distance from target
		# and if 2 damages everything but the position
		for x in range(x_len):
			for y in range(y_len):
				if (damage >= 0 and self.distance(target_x, target_y) > 4):
				or (damage >= 1 and submarine.distance(x, y, target_x, target_y) > 1)
				or (damage >= 2 and submarine.distance(x, y, target_x, target_y) > 0):
					self.possible_positions[x][y] = 0


	def sonar_to_order(self, zone, result):
		# Remove this zone from the possible position

	def sonar_to_me(self, zone, result):
		# Remove this zone from the possible position

	def distance(self, x2, y2):

	def distance(x1, y1, x2, y2):


# Opponent
class opponent(submarine):


# Me
class me(submarine):

	def __init__(self, x, y):
		self.position_x = x
		self.position_y = y

	


# Grid content and user id
width, height, my_id = [int(i) for i in input().split()]

grid = []
for i in range(height):
    grid[i] = [e!='x' for e in list(input())]

print(grid)

# Starting position
print("7 7")

# Game loop
while True:
    x, y, my_life, opp_life, torpedo_cooldown, sonar_cooldown, silence_cooldown, mine_cooldown = [int(i) for i in input().split()]
    sonar_result = input()
    opponent_orders = input()

    # Parse opponent order
    opponent_orders_list = opponent_orders.split(sep='|')

    for opponent_order in opponent_orders_list:
    	opponent_order_splitted = opponent_order.split()
		opponent_order_command = opponent_order_splitted[0]

		if opponent_order_command=='MOVE':
			opponent_direction = opponent_order_splitted[1]

		elif opponent_order_command=='SURFACE':


		elif opponent_order_command=='TORPEDO':
			opponent_torpedo_x = opponent_order_splitted[1]
			opponent_torpedo_y = opponent_order_splitted[2]

    # Calculate opponent possible position


    # Calculate opponent knowledge on my positon

    # Calculate available next position cost for discovery (removing position from list of guess)

    # Calculate next position cost for movement (removing map availability)

    # Calculate best discovery move and benefit (number of position removed from list of guess)

    # Calcualte best attack move (chances of hit)

    # Pick best attack vs discovery action

    # Pick best next position in term of attack capabilities vs route cost

    # Launch command
    print("MOVE N TORPEDO")


    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)