from django.contrib import admin
from .models import *

# Register your models here.
class userregistrationadmin(admin.ModelAdmin):
    list=('username','email','password','cpassword')


admin.site.register(userregistration,userregistrationadmin)
admin.site.register(category)
admin.site.register(subcategory)
admin.site.register(product)


