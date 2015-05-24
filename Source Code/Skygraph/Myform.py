from django import forms
from django.contrib.auth.models import User   # fill in custom user info then save it
from django.contrib.auth.forms import UserCreationForm
from Skygraph.models import Userbkp

class MyRegistrationForm(UserCreationForm):
    email = forms.EmailField(required = True)
    first_name = forms.CharField(required = False)
    last_name = forms.CharField(required = False)
    city = forms.CharField(required = False)


    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def save(self,commit = True):
        user = super(MyRegistrationForm, self).save(commit = False)

        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.city = self.cleaned_data['city']

        userp = Userbkp( Fname= self.cleaned_data['first_name'], Lname=self.cleaned_data['last_name'], Email=self.cleaned_data['email'],
                             Uname=self.cleaned_data['username'], City=self.cleaned_data['city'])
        userp.save()

        if commit:
            user.save()

        return user