from google.cloud import datastore
import os
proj_id  = os.getenv('PROJ')
print (proj_id)

'''
client = datastore.Client(proj_id)
key = client.key("entitykind", 1234)
entity = datastore.Entity(key = key)

entity.update(
{
    'fppf':'dasd',
    'absd': 'dsa',
    'qux':False,
}
)
client.put(entity)

result = client.get(key)
print (result)
'''