from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from App.models import *
from App import app

api = Api(app)

class question(Resource):

	def post(self):
		try:
			question = request.get_json()['question'].strip()
		except KeyError:
			return jsonify({'message':'question must be provided'})
		if len(question) == 0:
			return jsonify({'message':'question can not be blank'})
		quests.append(question)
		return jsonify({"message":question})
        
	def get(self):
		return jsonify(quest_id(quests))

class questionId(Resource):

	def get(self, id):
		if id not in quests:
			return jsonify({'message':'question does not exeist'})
		else:
			return jsonify(quest_id(quests)[id])

api.add_resource(question, '/stackoverflow.com/api/v1/question/')
api.add_resource(questionId, '/stackoverflow.com/api/v1/questionId/<int:id>')				