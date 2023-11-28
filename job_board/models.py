from django.db import models

# Create your models here.
# model => python class
# model represents a table in the db. locally nu när vi skapar ett Django project, så använder den db.sqlite3 databas. Den sparas lokalt
# attributerna är the fields in the table.

class JobPost(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    company = models.CharField(max_length=100)
    salary = models.IntegerField()
    is_active = models.BooleanField(default=False)