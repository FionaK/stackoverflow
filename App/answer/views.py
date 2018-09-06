from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from App.models import *
from App import app

api = Api(app)

class answer(Resource):
	def post(self, id):
		try:
			answer = request.get_json()['answer']
		except KeyError:
			return jsonify({"message":"answer must be provided"})	
		if id not in give_id(quests):
			return jsonify({"message":"Can't post an answer,question does not exist"})
		if id in ans:
			ans[id].append(answer)
		else:
			ans.update({id:[answer]})
		return jsonify({give_id(quests)[id]:ans[id]})

api.add_resource(answer, '/stackoverflow.com/api/v1/answer/<int:id>')		