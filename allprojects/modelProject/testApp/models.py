from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
'''class Student(models.Model): # STUDENT
	name = models.CharField(max_length=100)
	rollno = models.IntergerField()


class Teacher(models.Model): # TEACHER
	name = models.CharField(max_length=100)
	ID = models.IntergerField()'''
#abstract model class
class ContactInfo(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    address = models.CharField(max_length=30)

    class Meta:
        abstract = True

class Customer(ContactInfo):
    phone = models.CharField(max_length=30)

class Staff(ContactInfo):
    position = models.CharField(max_length=30)

#Multi table inheritence
class Place(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    def __str__(self):
        return self.name
class Restaurant(Place):
    serves_tuna = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)
    def __bool__(self):
        return self.serves_tuna

class common(models.Model): # COMM0N
	name = models.CharField(max_length=100)

	class Meta:
		abstract = True

class std(common): # STUDENT
	rollno = models.IntegerField()


class tea(common): # TEACHER
	ID = models.IntegerField()


class Post(models.Model):
    STATUS_CHOICES=(('draft','Draft'),('published','Published'))
    title=models.CharField(max_length=264)
    slug=models.SlugField(max_length=264,unique_for_date='publish')
    author=models.ForeignKey(User,related_name='testApp_posts',on_delete=models.CASCADE,)
    body=models.TextField()
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)#datetime of create() action
    updated=models.DateTimeField(auto_now=True)#datetme of save() action
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')

    class Meta:
        ordering=('-publish',)
    def __str__(self):
        return self.title

class Comment(models.Model):
    post=models.ForeignKey(Post,related_name='comments',on_delete=models.CASCADE,)
    name=models.CharField(max_length=32)
    email=models.EmailField()
    body=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)
    class Meta:
        ordering=('created',)
    def __str__(self):
        return 'Commented By {} on {}'.format(self.name,self.post)
"""class AshokManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')

class AshokTable(models.Model):
    STATUS_CHOICES1=(('draft','Draft'),('published','Published'))
    title1=models.CharField(max_length=264)
    slug1=models.SlugField(max_length=264,unique_for_date='publish')
    author1=models.ForeignKey(User,related_name='testApp_posts',on_delete=models.CASCADE,)
    body1=models.TextField()
    publish1=models.DateTimeField(default=timezone.now)
    created1=models.DateTimeField(auto_now_add=True)#datetime of create() action
    updated1=models.DateTimeField(auto_now=True)#datetme of save() action
    status1=models.CharField(max_length=10,choices=STATUS_CHOICES1,default='draft')
    objects=AshokManager()

    class Meta:
        ordering=('-publish',)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail',args=[self.publish.year,
        self.publish.strftime('%m'),self.publish.strftime('%d'),self.slug])"""

class CustomManager(models.Manager):
	def get_queryset1(self):
		return super().get_queryset().order_by('eno')
	def get_emp_sal_range(self,esal1,esal2):
		return super().get_queryset().filter(esal__range=(esal1,esal2))
	def get_employees_sorted_by(self,param):
		return super().get_queryset().order_by(param)
class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=30)
    esal=models.FloatField()
    eaddr=models.CharField(max_length=30)
    objects=CustomManager()
    def __str__(self):
        return 'Employee object with eno: '+str(self.eno)

    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})

class CustomManager1(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(esal__gte=15000)

class CustomManager2(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('ename')

class CustomManager3(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(esal__lt=10000)

# Create your models here.
class Employee1(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=64)
    esal=models.FloatField()
    eaddr=models.CharField(max_length=256)
    objects=CustomManager1()

class ProxyEmployee(Employee1):
    objects=CustomManager2()
    class Meta:
        proxy=True

class ProxyEmployee2(Employee1):
    objects=CustomManager3()
    class Meta:
        proxy=True



'''class Student(models.Model):
    rollno=models.IntegerField()
    name=models.CharField(max_length=30)
    dob=models.DateField()
    marks=models.IntegerField()
    email=models.EmailField()
    phonenumber=models.IntegerField(15)
    address=models.TextField()
    class Meta:
        ordering=('rollno',)'''

class Movie(models.Model):
    rdate=models.DateField()
    moviename=models.CharField(max_length=30)
    hero=models.CharField(max_length=30)
    heroine=models.CharField(max_length=30)
    rating=models.IntegerField()

#    name=models.CharField(max_length=30)
#    quantity=models.IntegerField()

class Book(models.Model):
    title=models.CharField(max_length=300)
    author=models.CharField(max_length=30)
    pages=models.IntegerField()
    price=models.FloatField()

class Beer(models.Model):
    name=models.CharField(max_length=128)
    taste=models.CharField(max_length=128)
    color=models.CharField(max_length=128)
    price=models.FloatField()
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})
