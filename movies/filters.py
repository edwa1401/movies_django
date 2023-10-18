import django_filters
from movies.models import Film



class FilmFilter(django_filters.FilterSet):

    # genre_filter = django_filters.CharFilter(lookup_expr='iexact')
    # rating_filter = django_filters.NumberFilter(lookup_expr='gte')
    # year_filter = django_filters.NumberFilter(lookup_expr='iexact')

    class Meta:
        model = Film
        fields = {
            'genre': ['exact'],
            'rating': ['gte'],
            'year_of_issue': ['exact'],
            }