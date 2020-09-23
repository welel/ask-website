from django.conf.urls import url
from qa.views import (questions_list_all, question_and_answers,
                      question_add, delete_question, signup, signin,
                      log_out, delete_answer)

urlpatterns = [
    url(r'^$', questions_list_all),
    url(r'^signin\/', signin),
    url(r'^signup\/', signup),
    url(r'^ask\/', question_add),
    url(r'^question\/(?P<article_id>[0-9]+)\/$', question_and_answers),
    url(r'^new\/', questions_list_all),
    url(r'^logout\/', log_out),
    url(r'^delete_question\/', delete_question),
    url(r'^delete_answer\/', delete_answer)
    ]

