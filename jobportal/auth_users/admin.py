from django.contrib import admin

from .models import CustomMyUser,Hobby,Interest,Company,JobTitle,JobProfile,JobCategory,JobDescription,Notification,NotificationList,Skills,JobApplication

# from django.contrib.auth.admin import UserAdmin

# Register your models here

admin.site.site_header = 'JobPortal'
admin.site.index_title ='Apps'


admin.site.register(CustomMyUser)
admin.site.register(Hobby)
admin.site.register(Interest)
admin.site.register(Company)
admin.site.register(JobProfile)
admin.site.register(JobTitle)
admin.site.register(JobCategory)
admin.site.register(JobDescription)
admin.site.register(Notification)
admin.site.register(NotificationList)
admin.site.register(Skills)
admin.site.register(JobApplication)

