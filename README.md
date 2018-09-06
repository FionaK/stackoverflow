[![Build Status](https://travis-ci.org/FionaK/stackoverflow.svg?branch=develop)](https://travis-ci.org/FionaK/stackoverflow)
[![Maintainability](https://api.codeclimate.com/v1/badges/e22103c8d149bcab1002/maintainability)](https://codeclimate.com/github/FionaK/stackoverflow/maintainability)
[![Coverage Status](https://coveralls.io/repos/github/FionaK/stackoverflow/badge.svg?branch=develop)](https://coveralls.io/github/FionaK/stackoverflow?branch=develop)
# Stackoverflow
> Stackoverflow-lite is a platform where users can post questions, answers as well as view available list of answers and questions.
 
## Made With
   * python
      > flask
      > flask-restful

### How to run it
  > clone the repository first
```sh
git clone https://github.com/FionaK/My-Diary.git
```
* cd into the project folder

* create virtual environment
```sh
virtualenv venv
```
* activate the virtual environment
```sh
source venv/bin/activate
```
* run pip freeze > requirements.txt to install the required external modules

* install the required modules using the following command;
```sh
pip install -r requirements.txt
```
* Run
```sh
python run.py to start the server
```

| Endpoint | **Functionality** | **Method** |
| ------ | ------ |------ |
| **stackoverflow.com/api/v1/question/** | post a question |POST |
| **stackoverflow.com/api/v1/question/** | fetch all questions |GET |
| **stackoverflow.com/api/v1/questionId/<int:id>** | Fetch single question |GET |
| **stackoverflow.com/api/v1/answer/<int:id>** | answer a question |POST |

## heroku link
[stackoverflow-lite](https://stack1.herokuapp.com/stackoverflow.com/api/v1/question/)
