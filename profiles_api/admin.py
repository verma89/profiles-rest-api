from django.contrib import admin
from profiles_api import models
# Register your models here.

#registering UserProfile model to be viewed in admin profile
admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)
