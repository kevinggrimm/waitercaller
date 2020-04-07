import os
basedir = os.path.abspath(os.path.dirname(__file__))
base_url = "http://0.0.0.0:5000/"

test = True

class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'mysecret_key'
	test = True