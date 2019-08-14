from django.contrib import admin
from .models import Saloon,UserSaloon,Post,Like,Comment,Subscribed,Files
# Register your models here.
admin.site.register(Saloon)
admin.site.register(UserSaloon)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Post)
admin.site.register(Subscribed)
admin.site.register(Files)
