from django.db import models

#db superuser -
# username: shannon
# pw: jobmailer

class User(models.Model):
    email = models.CharField(max_length=100)# Users' emails
    signup_date = models.DateTimeField() #When added to database
    def __str__(self):
        return self.id + " " + self.email
class Topic(models.Model):
    name = models.CharField(max_length=100)# Topic name
    def __str__(self):
        return self.name
class UserTopic(models.Model):
    user_id = models.ForeignKey(User) #A link to a User object
    topic_id = models.ForeignKey(Topic) # A link to the Topic object
    last_update_time = models.DateTimeField() #last time updated
    def __str__(self):
        return self.user_id.email + " " + self.topic_id.name