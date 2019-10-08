from django.test import TestCase
import unittest
import alphabet
import generate
import string


class TestAlphabet(unittest.TestCase):
	# should return a full alphabet of valid characters
	def test_get_alpha(self):
		test_alpha = alphabet.Alphabet()
		self.assertEqual(test_alpha.get(), list(string.ascii_letters + string.digits))
		self.assertEqual(test_alpha.lookup(0), 'a')


class TestGenerate(unittest.TestCase):
	# work in progress
	def test_generte_url(self):
		self.assertEqual(0,0)

if __name__ == '__main__':
	unittest.main()