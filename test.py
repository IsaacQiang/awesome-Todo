from app.models import Todo
from flask.ext.mongoengine import MongoEngine

print type(Todo.objects.all())