import time
from math import floor
from alphabet import Alphabet

# URL structure:
# short.en/g8IndG1V
# [g8] is generated based off time of creation
# [IndG1V] is generated via randomization, collisions unlikely

class URL():

	def __init__(self):
		self.creation_time = time.time()

	def time_stamp_calc(self):
		time = floor(self.creation_time)
		# choosing a seed value to compare, in this case, the date im writing this code
		seed = 10012019
		alpha = Alphabet()
		alpha.shuffle()
		index = (time % seed)
		# digit_one = alpha[temp_time % seed]
		# alpha = alpha.shuffle()
		# digit_two = alpha[temp_time % seed]

		return index
		# WIP

temp = URL()
print(temp.time_stamp_calc())

