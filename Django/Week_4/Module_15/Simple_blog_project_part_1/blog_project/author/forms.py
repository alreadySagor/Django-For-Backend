from django import forms
from . models import Author

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__' # sobkichu niyei ekta form toiri hoye jabe
        # fields = ['name', 'bio'] # name ar bio niye ekta form toiri hoye jabe
        # exclude = ['bio'] # bio ta bad diye baki ja kichu ache segula niye ekta form toiri hoye jabe.