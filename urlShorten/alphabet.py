import string
from random import shuffle


class Alphabet():

	base_alphabet = string.ascii_letters + string.digits


	def __init__(self):
		self._alphabet = Alphabet.base_alphabet

	def get(self: string):
		return self._alphabet

	def lookup(self, index: string):
		return self._alphabet[index]

	def shuffle(self: string):
		alpha = list(self._alphabet)
		shuffle(alpha)
		return alpha

