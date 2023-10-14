from django import forms
from movies.models import Film

class FilteredFilmsForm(forms.Form):

    genres = forms.ChoiceField(choices=Film.Genre.choices)
    ratings = forms.FloatField()
    years_of_issue = forms.IntegerField(min_value=0, max_value=10)
