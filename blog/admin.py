from django.contrib import admin

# Register your models here.
#6th step
from .models import Post


#admin.site.register(product)
#7th

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','file','content','date_posted')


admin.site.register(Post,PostAdmin)