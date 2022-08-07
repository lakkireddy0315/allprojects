from django.contrib import admin
from testApp.models import Employee,Student
from testApp.models import Author,Book
from testApp.models import hydjobs,blorejobs,chennaijobs,punejobs
#from testApp.serializers import BookSerializer

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['id','eno','ename','esal','eaddr']

admin.site.register(Employee,EmployeeAdmin)

class StudentAdmin(admin.ModelAdmin):
	list_display=['id','name','rollno','marks','gf','bf']
admin.site.register(Student,StudentAdmin)

from testApp.models import Author,Book
class AuthorAdmin(admin.ModelAdmin):
    list_display=('id','first_name','last_name','subject')
class BookAdmin(admin.ModelAdmin):
    list_display=('id','title','author','release_date','rating')

admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)

class hydjobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']

class blorejobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']

class chennaijobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']

class punejobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']

admin.site.register(hydjobs,hydjobsAdmin)
admin.site.register(chennaijobs,chennaijobsAdmin)
admin.site.register(blorejobs,blorejobsAdmin) 
admin.site.register(punejobs,punejobsAdmin)
