from flask_login import UserMixin

MOCK_USERS = [
	{
		'email': 'test@example.com',
		'salt': '123456',
		'hashed': ''
	}
]

class MockDBHelper:
	
	def get_user(self, email):
		user = [x for x in MOCK_USERS if x.get("email") == email]
		if user:
			return user[0]
		return None

	def add_user(self, email, salt, hashed):
		MOCK_USERS.append({
				'email': email, 
				'salt': salt,
				'hashed': hashed
			})


class User(UserMixin):
	
	def __init__(self, email):
		self.email = email

	def get_id(self):
		return self.email

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def is_authenticated(self):
		return True