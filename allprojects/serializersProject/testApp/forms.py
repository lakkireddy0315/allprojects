from testApp.models import Student
from django import forms
from django.contrib.auth.models import User
class StudentForm(forms.ModelForm):
	def clean_marks(self):
		inputmarks=self.cleaned_data['marks']
		if inputmarks < 35:
			raise forms.ValidationError('Marks should be >= 35')
		return inputmarks
	class Meta:
		model=Student
		fields='__all__'

class SignUpForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','email','first_name','last_name']
