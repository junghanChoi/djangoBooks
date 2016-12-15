from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published') # verbose text shows in admin

    def __unicode__(self): # __str__ on Python3
        return self.question_text
    # table description.
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    # question_id is foreign key, so assign it, then id comes
    def __unicode__(self):  # __str__ on Python3
        return self.choice_text

    def __str__(self):
        return self.choice_text
