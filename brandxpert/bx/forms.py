from django import forms


# Form to map with html input fields
class write(forms.Form):
    """ Form class for the write view """
    info = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
