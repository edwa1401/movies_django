from django.urls import path
from movies.views import FilmDetailView, FilmListView, FilmCreateView, FilmDeleteView, FilmListFilterView

app_name = 'movies'

urlpatterns = [
    path('<int:pk>/', FilmDetailView.as_view(), name='detail'),
    path('', FilmListView.as_view(), name='film_list'),
    path('create/', FilmCreateView.as_view()),
    path('<int:pk>/delete/', FilmDeleteView.as_view()),
    path('filter/', FilmListFilterView.as_view(), name='film_filter'),
]