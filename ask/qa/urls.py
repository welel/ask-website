from django.conf.urls import url
from qa.views import test, questions_list_all, questions_list_popular, question_display

urlpatterns = [
    url(r'^$', questions_list_all),
    url(r'^login\/', test),
    url(r'^signup\/', test),
    url(r'^ask\/', test),
    url(r'^question\/(?P<article_id>[0-9]+)\/$', question_display),
    url(r'^popular\/', questions_list_popular),
    url(r'^new\/', test),
    ]

