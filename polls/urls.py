from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.show, name='show'),
    path('<int:question_id>/vote', views.vote, name='vote'),
    path('<int:question_id>/add_vote', views.add_vote, name='add_vote'),
    path('<int:question_id>/result', views.results, name='results')
]