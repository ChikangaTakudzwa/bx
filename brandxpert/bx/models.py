from django.db import models
from datetime import datetime

services = (("Logo", "logo"), ("Graphic Design", "graphics"), ("Info Graphics", "info"))

# Create your models here.
class Work(models.Model):
    """ Model for portfolio items """
    file_name = models.CharField(max_length=50, help_text="Name *name must start with logo_, graphic_ or info_")
    image = models.ImageField(upload_to ='bx/media', help_text="Image")
    service_type = models.CharField(max_length=50, choices=services, default=1, help_text="Service Type")
    date_uploaded = models.DateField(default=datetime.now, blank=True, help_text="Date uploaded")

    def __str__(self):
        """String for representing the Model object."""
        return str(self.file_name)


class Motion(models.Model):
    """ Model for motion graphics """
    motion_name = models.CharField(max_length=50, help_text="Motion Name")
    link = models.URLField(max_length=200, help_text="Source Link/Youtube Link")
    date_uploaded = models.DateField(default=datetime.now, blank=True, help_text="Date uploaded")

    def __str__(self):
        """String for representing the Model object."""
        return str(self.motion_name)
