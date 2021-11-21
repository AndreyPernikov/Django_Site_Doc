from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),  # Http/polls/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),  # Http/polls/1/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),  # Http/polls/1/results/
    path('<int:question_id>/vote/', views.vote, name='vote'),  # Http/polls/1/vote/
]
