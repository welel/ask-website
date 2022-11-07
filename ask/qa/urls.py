from django.urls import path
from .views import (
     questions_list_all,
     question_and_answers,
     add_question,
     delete_question,
     signup,
     signin,
     log_out,
     delete_answer,
     add_answer,
     load_questions
)

urlpatterns = [
    path('', questions_list_all, name='root'),
    path('signin/', signin, name='login'),
    path('signup/', signup, name='register'),
    path('logout/', log_out, name='logout'),
    path('ask/', add_question, name='add_question'),
    path('question/<int:question_id>/', question_and_answers, name='question'),
    path('question/<int:question_id>/delete/', delete_question, 
          name='delete_question'),
    path('question/<int:question_id>/add_answer', add_answer,
          name='add_answer'),
    path('question/delete_answer/<int:answer_id>/', delete_answer,
          name='delete_answer'),
    path('questions/ajax/load_more/', load_questions, name='load_more'),
]
