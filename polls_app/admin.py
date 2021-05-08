from django.contrib import admin
from django.contrib.admin import TabularInline
from .models import Polls, Questions, Answers


@admin.register(Answers)
class AnswersAdmin(admin.ModelAdmin):
    pass


class AnswersInline(TabularInline):
    show_change_link = True
    model = Answers
    # extra = 1


@admin.register(Questions)
class QuestionAdmin(admin.ModelAdmin):
    pass


class QuestionInline(TabularInline):
    show_change_link = True
    model = Questions
    extra = 0


@admin.register(Polls)
class PollsAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]

# class InlineModelExistingInline(admin.TabularInline):
#     model = InlineModel
#     readonly_fields = ('data', 'user') #All Fields here except pk
#     can_delete = False
#     extra = 0
#     max_num = 0
