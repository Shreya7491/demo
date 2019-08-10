from django.urls import include, path

from . import views

urlpatterns = [
    path('question/', views.QuestionListView.as_view()),
    path('start/', views.start),
    path('generate/', views.generate),
    path('show/', views.show),
    path('identify/', views.identify),

]
