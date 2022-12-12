from django.contrib import admin
from .models import WorksTable, MotionTable

# Register your models here.
@admin.register(WorksTable)
class WorksAdmin(admin.ModelAdmin):
    """ WorksTable Admin Reg """
    list_display = ("file_name", "image", "serviceType", "date_uploaded")

# admin.site.register()

@admin.register(MotionTable)
class MotionAdmin(admin.ModelAdmin):
    """ MotionTable Admin Reg """
    list_display = ("motion_name", "motion_link", "linkThumbnail", "date_uploaded")

# admin.site.register(MotionTable)
