from django.db import models
from datetime import datetime

services = (("Logo", "logo"), ("Graphic Design", "graphics"), ("Info Graphics", "info"))

class Meta:
    managed = True


# Create your models here.
class WorksTable(models.Model):
    """ Model for portfolio items """
    file_name = models.CharField(max_length=50, help_text="Name *name must start with logo_, graphic_ or info_")
    image = models.ImageField(upload_to ='bx/media', help_text="Image to show")  # noqa: E251
    serviceType = models.CharField(max_length=50, choices=services, default=1, help_text="Service Type")
    date_uploaded = models.DateField(default=datetime.now, blank=True, help_text="Date uploaded")


    def __str__(self):
        """String for representing the Model object."""
        return str(self.file_name)


class MotionTable(models.Model):
    """ Model for motion graphics """
    motion_name = models.CharField(max_length=50, help_text="Motion Name")
    linkThumbnail = models.ImageField(upload_to ='bx/media', help_text="Image")  # noqa: E251
    motion_link = models.URLField(max_length=200, help_text="Youtube Link")
    date_uploaded = models.DateField(default=datetime.now, blank=True, help_text="Date uploaded")


    def __str__(self):
        """String for representing the Model object."""
        return str(self.motion_name)
