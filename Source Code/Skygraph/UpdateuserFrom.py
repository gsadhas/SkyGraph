from django import forms
from Skygraph.models import Userbkp

class UserUpdateFor(forms.Form):
    nfname = forms.CharField(label='nfname', max_length=20)
    nlname = forms.CharField(label='nlname', max_length=20)
    ncity = forms.CharField(label='ncity', max_length=20)







