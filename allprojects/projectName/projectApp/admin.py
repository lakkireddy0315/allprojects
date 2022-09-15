from django.contrib import admin
from .models import Post,Item,Customer,Purchase,Album,Song,Author,Book,Vehicle,Car

# Register your models here.
class AlbumAdmin(admin.ModelAdmin):
    model=Album

admin.site.register(Album,AlbumAdmin)

class SongAdmin(admin.ModelAdmin):
    model=Song

admin.site.register(Song,SongAdmin)

class AuthorAdmin(admin.ModelAdmin):
    model=Author

admin.site.register(Author,AuthorAdmin)

class BookAdmin(admin.ModelAdmin):
    model=Book

admin.site.register(Book,BookAdmin)

class VehicleAdmin(admin.ModelAdmin):
    model=Vehicle

admin.site.register(Vehicle,VehicleAdmin)

class CarAdmin(admin.ModelAdmin):
    model=Car

admin.site.register(Car,CarAdmin)

class PostAdmin(admin.ModelAdmin):
    model=Post

admin.site.register(Post,PostAdmin)


class ItemAdmin(admin.ModelAdmin):
    model=Item

admin.site.register(Item,ItemAdmin)

class CustomerAdmin(admin.ModelAdmin):
    model=Customer

admin.site.register(Customer,CustomerAdmin)

class PurchaseAdmin(admin.ModelAdmin):
    model=Purchase

admin.site.register(Purchase,PurchaseAdmin)
