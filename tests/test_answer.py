import unittest
from flask import json, request
import os,sys
sys.path.insert(0, os.path.abspath(".."))
from App.answer.views import *

class TestQuestion(unittest.TestCase):

	client = app.test_client()

	def setUp(self):
		self.quest = []
		self.ans = {}
		data = json.dumps({
			"question":"can this be done"
			})
		header = {"Content-type" : "application/json"}
		quest = self.client.post("/stackoverflow.com/api/v1/question/", data=data, headers=header)
		response = quest.get_json()
		self.quest.append(response)


	def test_post_answer(self):
		data = json.dumps({
			"answer":"this won't work"
			})
		header = {"Content-type" : "application/json"}
		post_response = self.client.post("/stackoverflow.com/api/v1/answer/1", data=data, headers=header)
		response = post_response.get_json()
		self.assertEqual(response, {'can this be done': ["this won't work"]})

	def test_empty_answer(self):
		data = json.dumps({
			})
		header = {"Content-type" : "application/json"}
		post_response = self.client.post("/stackoverflow.com/api/v1/answer/11", data=data, headers=header)
		response = post_response.get_json()
		self.assertEqual(response, {'message': 'answer must be provided'})

	def test_answer_without_question(self):
		data = json.dumps({
			"answer":"it is possible"
			})
		header = {"Content-type" : "application/json"}
		post_response = self.client.post("/stackoverflow.com/api/v1/answer/11", data=data, headers=header)
		response = post_response.get_json()
		self.assertEqual(response, {'message': "Can't post an answer,question does not exist"})

	def test_wrong_method(self):
		data = json.dumps({
			"answer":"it is possible"
			})
		header = {"Content-type" : "application/json"}
		post_response = self.client.get("/stackoverflow.com/api/v1/answer/1", data=data, headers=header)
		response = post_response.get_json()
		self.assertEqual(response, {'message': 'The method is not allowed for the requested URL.'})

	def test_invalid_url(self):
		response = self.client.get('/stackoverflow.com/ap1/v1/question/')
		self.assertEqual(response.status_code, 404)