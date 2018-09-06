from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from App.models import *
from App import app

api = Api(app)

class question(Resource):
	def post(self):
		question = request.get_json()['question']
		quests.append(question)
		return jsonify({"message":question})

	def get(self):
		return jsonify(give_id(quests))

class questionId(Resource):
	def get(self, id):
		return jsonify(give_id(quests)[id])

api.add_resource(question, '/stackoverflow.com/api/v1/question/')
api.add_resource(questionId, '/stackoverflow.com/api/v1/questionId/<int:id>')				