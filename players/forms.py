from django import forms

class PlayerQueryForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=False,
        label='Player Name',
        widget=forms.TextInput(attrs={'placeholder': 'Enter player name'})
    )
    dob = forms.IntegerField(
        required=False,
        label='Year of Birth',
        widget=forms.NumberInput(attrs={'placeholder': 'Enter year of birth (YYYY)'})
    )
    hand = forms.CharField(
        max_length=1,
        required=False,
        label='Handedness',
        widget=forms.TextInput(attrs={'placeholder': 'Enter hand (e.g., R or L)'})
    )
    ioc = forms.CharField(
        max_length=3,
        required=False,
        label='Country Code (IOC)',
        widget=forms.TextInput(attrs={'placeholder': 'Enter country code (e.g., USA, FRA)'})
    )
    height = forms.IntegerField(
        required=False,
        label='Height (cm)',
        widget=forms.NumberInput(attrs={'placeholder': 'Enter height in cm'})
    )
    wikidata_id = forms.CharField(
        max_length=50,
        required=False,
        label='Wikidata ID',
        widget=forms.TextInput(attrs={'placeholder': 'Enter Wikidata ID'})
    )
