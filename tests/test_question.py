import unittest
import os,sys
sys.path.insert(0, os.path.abspath(".."))
from App.question.views import *

class TestQuestion(unittest.TestCase):
	def setUp(self):
		self.app = app.test_client()
	def test_post(self):
		response1 = self.app.put('/stackoverflow.com/api/v1/question/', json = {"question":"how to document in apiary"})
		response = self.app.post('/stackoverflow.com/api/v1/question/', json = {"question":"how to document in apiary"})
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.get_json()["message"], "how to document in apiary")
		self.assertEqual(response1.status_code, 405)

	def test_get(self):
		response = self.app.get('/stackoverflow.com/api/v1/question/')
		self.assertEqual(response.status_code, 200)