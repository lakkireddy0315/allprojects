from django import forms
#from testApp.models import Employee

class GeeksForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
    views = forms.IntegerField()
    available = forms.BooleanField()
'''class SampleForrm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()  '''
