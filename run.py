from App import app
from App.question.views import *
from App.answer.views import *

if __name__ == '__main__':
	app.run(debug=True)