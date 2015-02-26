import unittest
from simplejobmarket.models import UserModel

class UserModelTestCase(unittest.TestCase):
	def test_password_setters(self):
		u = UserModel(password='cat')
		self.assertTrue(u.passwordhash is not None)

	def test_no_password_getter(self):
		u = UserModel(password='cat')
		with self.assertRaises(AttributeError):
			u.password

	def test_password_verification(self):
		u = UserModel(password='cat')
		self.assertTrue(u.verify_password('cat'))
		self.assertFalse(u.verify_password('dog'))

	def test_password_salts_random(self):
		u = UserModel(password='cat')
		u2 = UserModel(password='cat')
		self.assertTrue(u.password_hash != u2.password_hash)