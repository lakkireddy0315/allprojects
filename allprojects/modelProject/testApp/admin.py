from django.contrib import admin
from testApp.models import Employee
from testApp.models import Movie,Book,Beer,Customer,Staff,Place,Restaurant
from testApp.models import Employee1,ProxyEmployee,ProxyEmployee2,Post,Comment#,AshokTable


# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    list_display=('name','email','post','body','created','updated','active')
    list_filter=('active','created','updated')
    search_fields=('name','email','body')

admin.site.register(Comment,CommentAdmin)

"""class AshokTableAdmin(admin.ModelAdmin):
    list_display=['title1','slug1','author1','publish1','created1','updated1','status1']
    list_filter=('status1','created1','publish1','author1')
    search_fields=('title1','body1')
    prepopulated_fields={'slug1':('title1',)}
    raw_id_fields=('author1',)
    ordering=['status1','publish1']

admin.site.register(AshokTable,AshokTableAdmin)"""

admin.site.register(Customer)
admin.site.register(Staff)
admin.site.register(Place)
admin.site.register(Restaurant)

class PostAdmin(admin.ModelAdmin):
    list_display=['title','slug','author','publish','created','updated','status']
    list_filter=('status','created','publish','author')
    search_fields=('title','body')
    prepopulated_fields={'slug':('title',)}
    raw_id_fields=('author',)
    ordering=['status','publish']

admin.site.register(Post,PostAdmin)

class Employee1Admin(admin.ModelAdmin):
    list_display=['eno','ename','esal','eaddr']

class ProxyEmployeeAdmin(admin.ModelAdmin):
    list_display=['eno','ename','esal','eaddr']

class ProxyEmployee2Admin(admin.ModelAdmin):
    list_display=['eno','ename','esal','eaddr']

admin.site.register(Employee1,Employee1Admin)
admin.site.register(ProxyEmployee,ProxyEmployeeAdmin)
admin.site.register(ProxyEmployee2,ProxyEmployee2Admin)

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['eno','ename','esal','eaddr']
    list_filter=('eno','id')
    search_fields=('eno',)
    ordering=('id',)
admin.site.register(Employee,EmployeeAdmin)

'''class StudentAdmin(admin.ModelAdmin):
    list_display=['rollno','name','dob','marks','email','phonenumber','address']

admin.site.register(Student,StudentAdmin)'''

class MovieAdmin(admin.ModelAdmin):
    list_display=['rdate','moviename','hero','heroine','rating']

admin.site.register(Movie,MovieAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display=['title','author','pages','price']

admin.site.register(Book,BookAdmin)

class BeerAdmin(admin.ModelAdmin):
    list_display=['name','taste','color','price']

admin.site.register(Beer,BeerAdmin)
