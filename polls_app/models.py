from django.db import models
from django.utils.translation import gettext_lazy as _


class Answers(models.Model):
    text = models.TextField(max_length=100, help_text='Answer')

    def __str__(self):
        return self.text


class Polls(models.Model):
    name = models.CharField(max_length=64)
    created_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    desc = models.TextField(max_length=100, help_text='Poll description')
    received_answers = models.JSONField(default=list, blank=True)

    def __str__(self):
        return self.name


class Questions(models.Model):

    QuestionType = [
            (0, 'Text Answer'),
            (1, 'One Answer'),
            (2, 'Multi Answers')
        ]
    text = models.TextField(max_length=64, help_text='Question')
    type = models.IntegerField(choices=QuestionType)
    answers = models.ManyToManyField(Answers, related_name='questions', null=True, blank=True)
    polls = models.ForeignKey(Polls, on_delete=models.SET_NULL, related_name='questions', null=True, blank=True)

    def get_display_type(self):
        return dict(Questions.QuestionType)[self.type]

    def __str__(self):
        return self.text
