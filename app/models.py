import datetime
from flask_login import UserMixin

MOCK_USERS = [
	{
		'email': 'test@example.com',
		'salt': '123456',
		'hashed': ''
	}
]

MOCK_TABLES = [
	{
		"_id": "1",
		"number": "1",
		"owner": "test@example.com",
		"url": "mockurl"
	}
]

MOCK_REQUESTS = [
	{
		"_id": "1",
		"table_number": "1",
		"table_id": "1",
		"time": datetime.datetime.now()
	}
]

class MockDBHelper:
	
	def get_user(self, email):
		user = [x for x in MOCK_USERS if x.get("email") == email]
		if user:
			return user[0]
		return None

	def get_tables(self, owner_id):
		return MOCK_TABLES

	def get_requests(self, owner_id):
		return MOCK_REQUESTS

	def add_user(self, email, salt, hashed):
		MOCK_USERS.append({
				'email': email, 
				'salt': salt,
				'hashed': hashed
			})

	def add_table(self, number, owner):
		MOCK_TABLES.append(
				{
					"_id": str(number),
					"number" : number,
					"owner": owner
				}
			)
		return number

	def add_request(self, _id, time):
		MOCK_REQUESTS.append(
				{
					"_id": _id,
					"table_number": _id,
					"time": time
				}
			)

	def update_table(self, _id, url):
		for table in MOCK_TABLES:
			if table.get("_id") == _id:
				table["url"] = url
				break

	def delete_request(self, request_id):
		for i, request in enumerate(MOCK_REQUESTS):
			if request.get("_id") == request_id:
				del MOCK_REQUESTS[i]
				break

	def delete_table(self, table_id):
		for i, table in enumerate(MOCK_TABLES):
			if table.get("_id") == table_id:
				del MOCK_TABLES[i]
				break 

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