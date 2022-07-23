from django import forms

class ReviewForm(forms.Form):
    first_name = forms.CharField(label="First Name" , max_length=15)
    last_name = forms.CharField(label="Last Name",max_length=15)
    email = forms.EmailField(label="Email")
    review = forms.CharField(label="Please Review here")