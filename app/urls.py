from app.views import TextListAndInsert, WordsListAndInsert

from django.urls import path

urlpatterns = [
    path('', TextListAndInsert.as_view()),
    path('words', WordsListAndInsert.as_view()),
]