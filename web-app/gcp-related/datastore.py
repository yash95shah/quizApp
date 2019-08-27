import os
project_id = os.getenv('GCLOUD_PROJECT')
from flask import current_app
from google.cloud import datastore

datastore_client = datastore.Client(project_id)

def list_entities(quiz= 'celebs', redact=True):
    return []

def save_question(question):
    key = datastore_client.key('Question')
    q_entity = datastore.Entity(key=key)
    for q_prop, q_val in question.iteritems():
        q_entity[q_prop] = q_val
    datastore_client.put(q_entity)