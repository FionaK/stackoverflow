from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

quests = []
ans = {}

class question(Resource):
	def post(self):
		question = request.get_json()['question']
		quests.append(question)
		return jsonify({'message':'question successfully posted'})

api.add_resource(question, '/stackoverflow.com/api/v1/question/')

if __name__ == '__main__':
	app.run(debug=True)