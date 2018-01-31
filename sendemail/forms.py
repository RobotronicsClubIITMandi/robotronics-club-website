from django import forms

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    first = forms.CharField(required=True)
    last = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
