from bson.objectid import ObjectId
import datetime
from flask_login import UserMixin
import pymongo

DATABASE = "waitercaller"

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

class DBHelper:

	def __init__(self):
		client = pymongo.MongoClient()
		self.db = client[DATABASE]

	def get_user(self, email):
		return self.db.users.find_one({"email": email})

	def add_user(self, email, salt, hashed):
		self.db.users.insert({"email": email, "salt": salt, "hashed": hashed})

	def add_table(self, number, owner):
		new_id = self.db.tables.insert({"number": number, "owner": owner})
		return new_id

	def update_table(self, _id, url):
		self.db.tables.update({"_id": _id}, {"$set": {"url": url}})

	def get_tables(self, owner_id):
		return list(self.db.tables.find({"owner": owner_id}))

	def get_table(self, table_id):
		return self.db.table.find_one({"_id": ObjectId(table_id)})

	def delete_table(self, table_id):
		self.db.tables.remove({"_id": ObjectId(table_id)})

	def add_request(self, table_id, time):
		table = self.get_table(table_id)
		try: 
			self.db.requests.insert({"owner": table['owner'],
				"table_number": table['number'],
				"table_id": table['table_id'],
				"time": time})
			return True
		except pymongo.errors.DuplicateKeyError:
			return False 

	def get_requests(self, owner_id):
		return list(self.db.requests.find({"owner": owner_id}))

	def delete_request(self, request_id):
		self.db.requests.remove({"request_id": ObjectId(request_id)})


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