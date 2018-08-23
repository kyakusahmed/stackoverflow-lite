from flask import Flask, jsonify, json, url_for, Response
import flask_restful
from flask_restful import Api, Resource, reqparse, request


app = Flask(__name__)
api = flask_restful.Api(app)

questions = []


@app.route('/api/v1/questions', methods=['GET'])
def get_questions():
    if questions == []:
        return "No questions posted", 400
    else:
        return jsonify({"questions": questions})


@app.route('/api/v1/questions/<int:questionID>', methods=['GET'])
def get_one_question(questionID):
    if questions:
        for question in questions:
            if question['questionID'] == questionID:
                return jsonify(question)
    return jsonify({'Question {}'.format(questionID): 'Not Found'})


@app.route('/questions', methods=['POST'], endpoint='post_question')
def posts():

    parser = reqparse.RequestParser()
    parser.add_argument("question_title")
    parser.add_argument("question_id")
    parser.add_argument("description")
    args = parser.parse_args()

    for question in questions:
        if(args["question_title"] == question["question_title"]):
            return "Question with Title {} already exists".format(args["question_title"]), 400

        else:
            question = {
                "question_title": args["question_title"],
                "question_id": args["question_id"],
                "description": args["description"]
            }

            questions.append(question)

            return("questions": question), 201
                


@app.route('/questions/<question_id>', methods=['GET'])
def get_one_questions():
    for question in questions:
        if(["question_id"] == question["question_id"]):
            return question, 201
        else:
            return "Question not found", 400


@app.route('/questions/<question_id>', methods=['PUT'], endpoint='update-question')
def single_posts(question_id):
    parser = reqparse.RequestParser()
    parser.add_argument("question_title")
    parser.add_argument("question_id")
    parser.add_argument("description")
    parser.add_argument("answer")
    args = parser.parse_args()

    for question in questions:
        if(args["question_title"] == question["question_title"]):
            question["question_id"] == args["question_id"]
            question["description"] == args["description"]
            return question, 200

    question = {
        "question_title": args["question_title"],
        "question_id": args["question_id"],
        "description": args["description"]
    }
    question["answer"].append(question)
    return question, 201


@app.route('/questions/<question_id>', methods=['DELETE'], endpoint='end-question')
def delete(self, methods=["DELETE"]):
    parser = reqparse.RequestParser()
    parser.add_argument("question_title")
    args = parser.parse_args()
    global questions
    questions = [
        question for question in questions if question["question_title"] != args["question_title"]]
    return "{} is deleted.".format(args["question_title"]), 200


if __name__ == '__main__':
    app.run(debug=True)
