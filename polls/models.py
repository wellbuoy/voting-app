from django.db import models

# Create your models here.
class Question(models.Model):

    # CharField to store question text
    question_text = models.CharField(max_length=200)

    # DateTimeField to store publication date
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        # Return question_text when printed
        return self.question_text

class Choice(models.Model):

    # foreign key relation with Question model
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')

    # max length of choice text
    choice_text = models.CharField(max_length=200)

    # integer field for votes, default 0
    votes = models.IntegerField(default=0)

    def __str__(self):
        # Return choice_text when printed
        return self.choice_text
