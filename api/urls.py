# score/urls.py
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from api import views

urlpatterns = [
    path('scorelist/', views.ScoreList.as_view()),
    path('scores/', views.score_save),
    path('scoreshow/', views.scoreShow),

]
urlpatterns = format_suffix_patterns(urlpatterns)
