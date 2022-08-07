from django.db import models

# Create your models here.
class hydjobs(models.Model):
    date=models.DateField();
    company=models.CharField(max_length=100);
    title=models.CharField(max_length=100);
    eligibility=models.CharField(max_length=100);
    address=models.CharField(max_length=100);
    email=models.EmailField();
    phonenumber=models.IntegerField()

class blorejobs(models.Model):
    date=models.DateField();
    company=models.CharField(max_length=100);
    title=models.CharField(max_length=100);
    eligibility=models.CharField(max_length=100);
    address=models.CharField(max_length=100);
    email=models.EmailField();
    phonenumber=models.IntegerField()

class chennaijobs(models.Model):
    date=models.DateField();
    company=models.CharField(max_length=100);
    title=models.CharField(max_length=100);
    eligibility=models.CharField(max_length=100);
    address=models.CharField(max_length=100);
    email=models.EmailField();
    phonenumber=models.IntegerField()

class punejobs(models.Model):
    date=models.DateField();
    company=models.CharField(max_length=100);
    title=models.CharField(max_length=100);
    eligibility=models.CharField(max_length=100);
    address=models.CharField(max_length=100);
    email=models.EmailField();
    phonenumber=models.IntegerField()

class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=64)
    esal=models.FloatField()
    eaddr=models.CharField(max_length=64)

class Student(models.Model):
	name=models.CharField(max_length=64)
	rollno=models.IntegerField()
	marks=models.IntegerField()
	gf=models.CharField(max_length=64)
	bf=models.CharField(max_length=64)

class Author(models.Model):
    first_name=models.CharField(max_length=64)
    last_name=models.CharField(max_length=64)
    subject=models.CharField(max_length=64)
    def __str__(self):
        return self.first_name

class Book(models.Model):
    title=models.CharField(max_length=256)
    author=models.ForeignKey(Author,on_delete=models.CASCADE,related_name='books_by_author')
    release_date=models.DateField()
    rating=models.IntegerField()
    def __str__(self):
        return self.title
