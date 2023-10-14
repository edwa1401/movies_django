from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.views.generic import DetailView, ListView, CreateView, DeleteView, FormView
from django.urls import reverse_lazy
from movies.forms import FilteredFilmsForm

from movies.models import Film

class FilmDetailView(DetailView):
    model = Film
    template = 'film_detail.html'


class FilmListView(ListView):
    model = Film
    template = 'film_list.html'


class FilmListFilterView(ListView):
    model = Film
    template = 'film_filter.html'
    
    def get_queryset(self) -> QuerySet[Any]:
        genre_filter = self.request.GET.get('genre_filter')
        new_context = Film.objects.filter(genre=genre_filter)
        return new_context
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super(FilmListFilterView, self).get_context_data(**kwargs)
        context['genre_filter'] = self.request.GET.get('genre_filter')
        return context


class FilmCreateView(CreateView):
    model = Film
    fields = ['title', 'description', 'genre', 'year_of_issue', 'rating', 'cover']


class FilmDeleteView(DeleteView):
    model = Film
    success_url = reverse_lazy('movies:film_list')

