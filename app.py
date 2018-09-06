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
		
ans = {}

class question(Resource):
	def post(self):
		question = request.get_json()['question']
		quests.append(question)
		return jsonify(question)

	def get(self):
		return jsonify(give_id(quests))

class questionId(Resource):
	def get(self, id):
		return jsonify(give_id(quests)[id])

class answer(Resource):
	def post(self, id):
		answer = request.get_json()['answer']
		if id not in give_id(quests):
			return jsonify({"message":"Can't post an answer,question does not exist"})
		if id in ans:
			ans[id].append(answer)
		else:
			ans.update({id:[answer]})
		return jsonify({give_id(quests)[id]:ans[id]})			

api.add_resource(question, '/stackoverflow.com/api/v1/question/')
api.add_resource(questionId, '/stackoverflow.com/api/v1/questionId/<int:id>')
api.add_resource(answer, '/stackoverflow.com/api/v1/answer/<int:id>')

if __name__ == '__main__':
	app.run(debug=True)
