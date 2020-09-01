from django.conf.urls import url
from qa.views import test

urlpatterns = [
    url(r'^$', test),
    url(r'^login\/', test),
    url(r'^signup\/', test),
    url(r'^ask\/', test),
    url(r'^question\/(?P<article_id>[0-9]+)\/', test),
    url(r'^popular\/', test),
    url(r'^new\/', test),
    ]
