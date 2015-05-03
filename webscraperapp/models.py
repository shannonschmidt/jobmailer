from django.db import models
from signup_app.models import Topic

__author__ = 'shannon'

class Job(models.Model):
    posting_date = models.DateField() #When posted
    found_date = models.DateField() #When our service first scraped this job
    company = models.CharField(max_length=100)#Company offering the job
    title = models.CharField(max_length=100)#Job title
    location = models.CharField(max_length=100)#Location of job
    source = models.CharField(max_length=100)#Where this job was found and scraped from
    link = models.CharField(max_length=200)#Link to job
    topics = models.ManyToManyField(Topic)
    def __str__(self):
        return str(self.posting_date) + ": " + self.company + " - " + self.title
    def get_topics(self):
        return '\n'.join([t.name for t in self.topics.all()])