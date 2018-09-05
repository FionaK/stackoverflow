from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

quests = []

def give_id(list):
	output = {}
	for each in list:
		output.update({list.index(each)+1:each})
	return output

class question(Resource):
	def post(self):
		question = request.get_json()['question']
		quests.append(question)
		return jsonify(question)

	def get(self):
		return jsonify(give_id(quests))	
		
api.add_resource(question, '/stackoverflow.com/api/v1/question/')

if __name__ == '__main__':
	app.run(debug=True)