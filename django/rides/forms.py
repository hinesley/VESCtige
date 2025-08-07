from django import forms


class RideUploadForm(forms.Form):
    file = forms.FileField()
