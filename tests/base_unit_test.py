from unittest import TestCase
import license_plate_recognition

class TestHelloWorld(TestCase):
	def test_is_string(self):
		string = license_plate_recognition.hello_world()
		self.assertTrue(isinstance(string,basestring))

