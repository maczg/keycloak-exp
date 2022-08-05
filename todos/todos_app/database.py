from flask_mongoengine import MongoEngine
from flask_redis import FlaskRedis

mongo = MongoEngine()
redis = FlaskRedis(decode_responses=True)