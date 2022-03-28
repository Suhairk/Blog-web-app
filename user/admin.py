from django.contrib import admin

# Register your models here.
#6th step
from .models import Profile


#admin.site.register(product)
#7th

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id','user_id','image')


admin.site.register(Profile,ProfileAdmin)