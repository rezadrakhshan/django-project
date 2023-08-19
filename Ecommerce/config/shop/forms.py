from django import forms
class ContactUsForm(forms.Form):
    message = forms.CharField(required=True,widget=forms.Textarea)
    name = forms.CharField(max_length=25, required=True)
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True,max_length=25)
    phone = forms.CharField(max_length=11,required=True)