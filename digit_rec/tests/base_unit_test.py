from unittest import TestCase
from digit_rec import digit_rec


class TestDigitRec(TestCase):
	def test_is_number(self):
		test_img_src = '/home/ajay/digit_rec/digit_rec/tests/pictures/0.png'
		digit = digit_rec.predict(test_img_src)
		print digit
		self.assertTrue(isinstance(digit,float))


