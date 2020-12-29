from django.contrib import admin

# Register your models here.
from .models import Vote, Link

admin.site.register(Vote)
admin.site.register(Link)