print("""\
TASK: Using composition create a program tha prints
      the sky with stars (* and .)
example: print_sky()   Enter:
 *   . *
.  .   
     * *
 * .  *.
. *  * .
""")

import random
print("\n----------- WITH Single Open/Close principle -----------")

class Star:
	def __init__(self):
		self.form = random.choice(["*", ".", ".", "."])
	def __str__(self):
		return self.form


class Sky:
	def __init__(self, size_x=9, size_y=5):
		self.size_x = size_x
		self.size_y = size_y
		self.sky = []
		# creating the sky:
		for y in range(self.size_y):
			self.sky.append([])
			for x in range(self.size_x):
				self.sky[y].append(" ")
		self.put_stars()

	def print_sky(self):
		for row in self.sky:
			for item in row:
				print(item, end="")
			print()
	
	def put_stars(self):
		stars = self.size_y * self.size_x // 2
		for s in range(stars):
			row = random.randrange(0, self.size_y)
			item = random.randrange(0, self.size_x)
			self.sky[row][item] = Star()


if __name__ == "__main__":
	sky = Sky(20, 10)
	sky.print_sky()

# Composition is applied in this program, we can see that:
# a sky "has" stars (composition)
# 
