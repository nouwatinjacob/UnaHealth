from django.urls import path

from . import views

app_name = "readings"
urlpatterns = [
    path('levels/', views.ReadingList.as_view()),
    path('levels/<int:pk>/', views.ReadingDetails.as_view()),
]