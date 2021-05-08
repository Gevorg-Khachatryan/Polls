from django.urls import path
from .views import PollsView, PollsListView

urlpatterns = [
    path('',PollsListView.as_view(),name='home-page'),
    # path(r'^/categories/$',CategoriesView.as_view(),name='categories-page'),
    # path(r'^/news/$',NewsListView.as_view(),name='news-page'),
    path(r'^/poll/(?P<pk>[0-9]+)/$', PollsView.as_view(), name='poll-page'),
    path(r'^/poll/save-answers/$', PollsView.save_answers, name='save-answers'),
    # path(r'^/category/(?P<category>[0-9]+)/$', HomeView.view_by_category, name='view-by-category')
]
