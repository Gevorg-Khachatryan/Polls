from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic, View
from .models import Polls, Questions, Answers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime
# Create your views here.


class PollsListView(generic.ListView):
    model = Polls
    context_object_name = 'polls'
    queryset = Polls.objects.filter(end_date__gt=datetime.datetime.now())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PollsView(generic.DetailView):
    model = Polls
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        poll = context['object']
        received_answers = []
        if poll.received_answers:
            for values in poll.received_answers[0].values():
                for key, value in values.items():
                    if isinstance(value, list):
                        received_answers.append([Questions.objects.get(pk=key),
                                                 Answers.objects.filter(pk__in=value).values_list('text')])
                    elif value and not value.isalpha():
                        received_answers.append([Questions.objects.get(pk=key), Answers.objects.get(pk=value)])
                    else:
                        received_answers.append([Questions.objects.get(pk=key), value])
        context['received_answers'] = received_answers
        return context

    @staticmethod
    def save_answers(request, **kwargs):
        poll_id = request.POST.get('poll_id')
        question_ids = request.POST.getlist('question_ids')
        answers_ids = request.POST.getlist('answer')
        multi_answers = request.POST.getlist('multi_answers')
        multi_question = request.POST.get('multi_question')

        user_answers = zip(question_ids, answers_ids) if question_ids and answers_ids else []
        answers_dict = {}
        for item in user_answers:
            if item[1]:
                answers_dict.update({item[0]: item[1]})
        if multi_answers and multi_question:
            answers_dict.update({multi_question: multi_answers})

        poll = Polls.objects.get(id=poll_id)
        data = poll.received_answers
        if not data:
            data.append({request.session.session_key: answers_dict})
        else:
            data[0].update({request.session.session_key: answers_dict})
        poll.received_answers = data
        poll.save()

        return HttpResponse('Success')
