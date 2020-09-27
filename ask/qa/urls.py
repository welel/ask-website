from django.urls import path
from .views import (questions_list_all, question_and_answers,
                      question_add, delete_question, signup, signin,
                      log_out, delete_answer)

urlpatterns = [
    path('', questions_list_all, name='root'),
    path('signin/', signin, name='login'),
    path('signup/', signup, name='register'),
    path('logout/', log_out, name='logout'),
    path('new/', questions_list_all, name='list_questions'),
    path('ask/', question_add, name='add_question'),
    path('question/<int:question_id>/',
         question_and_answers,
         name='question'),
    path('question/<int:question_id>/delete/',
         delete_question,
         name='delete_question'),
    path('question/delete_answer/<int:answer_id>/',
         delete_answer,
         name='delete_answer')
    ]

