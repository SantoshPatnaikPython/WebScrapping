from django import forms

class Web_Form(forms.Form):
    to_search = forms.CharField()
    number_of_images = forms.IntegerField()
    destination_folder = forms.CharField()
