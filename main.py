from google.cloud import datastore
import simplejson as json


def hello(request):
  
  return 'Hello World!'


def get_todo(request):
  
  client = datastore.Client()
  query = client.query(kind='Todo')
  
  result = ''

  for entity in query.fetch():
    result += str(entity['name']) + ','

  return result


def add_todo(request):
  
  data = json.loads(request.data.decode('utf-8'))
  
  client = datastore.Client()
  entity = datastore.Entity(key=client.key('Todo'))

  entity.update({
    'name': str(data['name'])
  })

  client.put(entity)

  return 'ok'