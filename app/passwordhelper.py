'''
get_hash()
--> wrapper of sha512 hash function
--> used to create final hash that we will store in database

get_salt()
--> generate cryptographically secure random string
--> encode as a base64 string
'''
import hashlib 
import os 
import base64

class PasswordHelper:

	def get_hash(self, plain):
		return hashlib.sha512((str(plain)).encode("utf-8")).hexdigest()

	def get_salt(self):
		return str(base64.b64encode(os.urandom(20)))

	def validate_password(self, plain, salt, expected):
		return self.get_hash(plain + salt) == expected
