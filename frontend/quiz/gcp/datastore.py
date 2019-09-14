import os
project_id = os.getenv('GCLOUD_PROJECT')
from flask import current_app
from google.cloud import datastore

datastore_client = datastore.Client(project_id)



def save_question(question):
    key = datastore_client.key('Question')
    q_entity = datastore.Entity(key=key)
    for q_prop, q_val in question.iteritems():
        q_entity[q_prop] = q_val
    datastore_client.put(q_entity)
    
def list_entities(quiz='gcp', redact=True):
    query = datastore_client.query(kind='Question')
    query.add_filter('quiz', '=', quiz)
    results =list(query.fetch())
    for result in results:
        result['id'] = result.key.id
    if redact:
        for result in results:
            del result['correctAnswer']
    return results


q = ["What is going on?","How are you doing this?"]
save_question(q)