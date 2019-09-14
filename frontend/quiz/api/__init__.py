import json

from flask import Response


from quiz.gcp import datastore, pubsub


def get_questions(quiz_name):
    questions = datastore.list_entities(quiz_name)
    payload = {'questions': list(questions)}
    payload = json.dumps(payload, indent=2, sort_keys=True)
    response = Response(payload)
    response.headers['Content-Type'] = 'application/json'
    return response

def get_grade(quiz_name, answers):
    questions = datastore.list_entities(quiz_name, False)
    score = len(list(filter(lambda x: x > 0,
                    list(map(lambda q:
                         len(list(filter(lambda answer:
                            answer['id'] == q['id'] and
                            int(answer['answer']) == q['correctAnswer'],
                            answers)))
                         , questions))
                )))
    payload = {'correct': score, 'total': len(questions)}
    payload = json.dumps(payload, indent=2, sort_keys=True)
    response = Response(payload)
    response.headers['Content-Type'] = 'application/json'
    return response