from django.urls import path, re_path
from qa.views import test

urlpatterns = [
    path('', test),
    path('login/', test),
    path('signup/', test),
    path('ask/', test),
    path('question/<int:article_id>/', test),
    path('popular/', test),
    path('new/', test),
    ]
