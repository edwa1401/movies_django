from typing import Any

from django.db.models import Q
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, FormView,
                                  ListView)
from django_filters.views import FilterView

from movies.filters import FilmFilter
from movies.forms import SearchFilmForm
from movies.models import Film


class FilmDetailView(DetailView):
    model = Film
    template_name = 'film_detail.html'


class FilmListFilterView(ListView):
    model = Film
    template_name = 'film_list.html'
    
    def get_queryset(self) -> QuerySet[Any]:
        genre_filter = self.request.GET.get('genre_filter')
        rating_filter = self.request.GET.get('rating_filter')
        year_filter = self.request.GET.get('year_filter')
        search_word = self.request.GET.get('search_word')

        qs = Film.objects

        if genre_filter:
            qs = qs.filter(genre=genre_filter)

        if rating_filter:
            qs = qs.filter(rating__gte=rating_filter)

        if year_filter:
            qs = qs.filter(year_of_issue=year_filter)

        if search_word:
            qs = qs.filter(
                Q(title__icontains=search_word)|
                Q(description__icontains=search_word))

        qs = qs.filter()
        return qs


    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['genre_filter'] = self.request.GET.get('genre_filter')
        context['rating_filter'] = self.request.GET.get('rating_filter')
        context['year_filter'] = self.request.GET.get('year_filter')
        context['search_word'] = self.request.GET.get('search_word')
        return context


class FilmCreateView(CreateView):
    model = Film
    fields = ['title', 'description', 'genre', 'year_of_issue', 'rating', 'cover']


class FilmDeleteView(DeleteView):
    model = Film
    success_url = reverse_lazy('movies:film_list')


class FilmFilterView(FilterView):
    model = Film
    filterset_class = FilmFilter
    template_name = 'film_filter.html'
    

class FilmSearchView(FormView):
    template_name = 'film_search.html'
    form_class = SearchFilmForm
    success_url = 'film_search'

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:

        search_form = self.form_class(request.GET)
        search_films = []

        if search_form.is_valid():
            search_data = search_form.cleaned_data['search_word']
            search_films = Film.objects.filter(
                Q(title__icontains=search_data)|
                Q(description__icontains=search_data))
            if not search_films:
                return HttpResponse('No movies with such words in title or description')

        return render(request, self.template_name, context={'form': search_form, 'search_films': search_films})
    