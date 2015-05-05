from django.db import models

#db superuser -
# username: admin
# pw: password

class Topic(models.Model):
    name = models.CharField(max_length=100)# Topic name
    def __str__(self):
        return self.name
class User(models.Model):
    email = models.CharField(max_length=100)# Users' emails
    signup_date = models.DateTimeField() #When added to database
    topics = models.ManyToManyField(Topic)
    def __str__(self):
        return str(self.id) + " " + self.email

    #used to display topics in the admin page
    def get_topics(self):
        return '\n'.join([t.name for t in self.topics.all()])
