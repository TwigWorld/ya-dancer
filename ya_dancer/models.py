from django.db import models
import mongoengine as mongo 

class HealthTable(models.Model):
	health_field = models.CharField(max_length=20)


class MongoHealthDocument(mongo.Document):
    health_field = mongo.StringField()
