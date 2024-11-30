from django import forms

class PlayerQueryForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=False,
        label='Player Name',
        widget=forms.TextInput(attrs={'placeholder': 'Enter player name'})
    )
    ranking = forms.IntegerField(
        required=False,
        label='Ranking',
        min_value=1,
        widget=forms.NumberInput(attrs={'placeholder': 'Enter player ranking'})
    )
    nationality = forms.CharField(
        max_length=50,
        required=False,
        label='Nationality',
        widget=forms.TextInput(attrs={'placeholder': 'Enter nationality'})
    )
