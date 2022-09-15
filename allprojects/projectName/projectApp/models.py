from django.db import models

# Create your models here.

STATUS_CHOICES = (
('draft', 'Draft'),
('published', 'Published'),
)

class Post(models.Model):
    title = models.CharField(max_length = 250)
    slug = models.SlugField(max_length = 250, null = True, blank = True)
    text = models.TextField()
    published_at = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    status = models.CharField(max_length = 10, choices = STATUS_CHOICES,
    													default ='draft')


    class Meta:
    	ordering = ('-published_at', )

    def __str__(self):
    	return self.title

from django.db import models

class Item(models.Model):
	name = models.CharField(max_length = 128)
	price = models.DecimalField(max_digits = 5, decimal_places = 2)

	def __str__(self):
		return self.name

class Customer(models.Model):
	name = models.CharField(max_length = 128)
	age = models.IntegerField()
	items_purchased = models.ManyToManyField(Item, through = 'Purchase')

	def __str__(self):
		return self.name

class Purchase(models.Model):
	item = models.ForeignKey(Item, on_delete = models.CASCADE)
	customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
	date_purchased = models.DateField()
	quantity_purchased = models.IntegerField()

from django.db import models

class Album(models.Model):
	title = models.CharField(max_length = 100)
	artist = models.CharField(max_length = 100)

class Song(models.Model):
	title = models.CharField(max_length = 100)
	album = models.ForeignKey(Album, on_delete = models.CASCADE)


from django.db import models

class Author(models.Model):
	name = models.CharField(max_length = 100)
	desc = models.TextField(max_length = 300)

class Book(models.Model):
	title = models.CharField(max_length = 100)
	desc = models.TextField(max_length = 300)
	authors = models.ManyToManyField(Author)

from django.db import models

class Vehicle(models.Model):
	reg_no = models.IntegerField()
	owner = models.CharField(max_length = 100)

class Car(models.Model):
	vehicle = models.OneToOneField(Vehicle,
		on_delete = models.CASCADE, primary_key = True)
	car_model = models.CharField(max_length = 100)
