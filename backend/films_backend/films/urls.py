from django.urls import path
from films.views import FilmListAPIView
from films.views import FilmDetailAPIView

urlpatterns = [
    # URL to get the films will be /api/films
    path('films/', FilmListAPIView.as_view()),
    path('films/<int:pk>/', FilmDetailAPIView.as_view())
]
