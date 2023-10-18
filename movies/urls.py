from django.urls import path
from movies.views import FilmDetailView, FilmCreateView, FilmDeleteView, FilmListFilterView, FilmFilterView, FilmSearchView

app_name = 'movies'

urlpatterns = [
    path('<int:pk>/', FilmDetailView.as_view(), name='detail'),
    path('create/', FilmCreateView.as_view()),
    path('<int:pk>/delete/', FilmDeleteView.as_view()),
    path('', FilmListFilterView.as_view(), name='film_list'),
    path('filter/', FilmFilterView.as_view(), name='film_filter'),
    path('search/', FilmSearchView.as_view(), name='film_search'),
]