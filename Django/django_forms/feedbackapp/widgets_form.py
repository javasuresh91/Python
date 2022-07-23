from django import forms

class WidgetsForm(forms.Form):
    email = forms.EmailField(label="Email")
    review = forms.CharField(label="Please Review here" , widget=forms.Textarea())
    feed = forms.CharField(label="Please Feedback me here" , widget=forms.TextInput(attrs={'class':'myform'}))