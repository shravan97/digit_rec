from unittest import TestCase
from license_plate_recognition import digit_rec


class TestDigitRec(TestCase):
	def test_is_number(self):
		test_img_src = '/home/ajay/license_plate_recognition/license_plate_recognition/tests/pictures/0.png'
		digit = digit_rec.predict(test_img_src)
		self.assertTrue(isinstance(digit,float))

	
