from django import forms
from django.core import validators
#from testApp.models import Student
from testApp.models import Movie,Employee
from django.contrib.auth.models import User

class EmployeeForm(forms.ModelForm):
	class Meta:
		model=Employee
		fields='__all__'

class EmailSendForm(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    to=forms.EmailField()
    comments=forms.CharField(required=False,widget=forms.Textarea)

class SignUpForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','email','first_name','last_name']

"""class StudentForm(forms.ModelForm):
     class Meta:
         model=Student
         fields='__all__'"""

class MovieForm(forms.ModelForm):
     class Meta:
         model=Movie
         fields='__all__'

class ItemAddForm(forms.Form):
      name=forms.CharField(max_length=30)
      quantity=forms.IntegerField()
class FeedbackForm(forms.Form):
    name=forms.CharField()
    rollno=forms.IntegerField()
    email=forms.EmailField()
    feedback=forms.CharField(widget=forms.Textarea)

    def clean(self):
        print('Total Form Validation by using single clean method...')
        total_cleaned_data=super().clean()
        inputname=total_cleaned_data['name']
        if inputname[0].lower() !='d':
            raise forms.ValidationError('Name should starts with d|D')
        inputrollno=total_cleaned_data['rollno']
        if inputrollno<=0:
            raise forms.ValidationError('Rollno should be >0')
class SignupForm(forms.Form):
    name=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
    rpassword=forms.CharField(label='Reenter Password',widget=forms.PasswordInput)

    email=forms.EmailField()

    def clean(self):
        total_cleaned_data=super().clean()
        pwd=total_cleaned_data['password']
        rpwd=total_cleaned_data['rpassword']
        if pwd != rpwd:
            raise forms.ValidationError('Both Passwords must be same')
