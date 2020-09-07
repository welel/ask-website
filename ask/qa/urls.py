from django.conf.urls import url
from qa.views import (questions_list_all,
        questions_list_popular, question_and_answers,
        question_add, signup, signin, log_out)

urlpatterns = [
    url(r'^$', questions_list_all),
    url(r'^signin\/', signin),
    url(r'^signup\/', signup),
    url(r'^ask\/', question_add),
    url(r'^question\/(?P<article_id>[0-9]+)\/$', question_and_answers),
    url(r'^popular\/', questions_list_popular),
    url(r'^new\/', questions_list_all),
    url(r'^logout\/', log_out)
    ]

