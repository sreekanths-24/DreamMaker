from django.db import models

# Create your models here.
class Events(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    startdate = models.DateTimeField(null=True, blank=True)
    enddate = models.DateTimeField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='event_images/', blank=True, null=True, default='default.jpg')

    def Meta(self):
        db_table = 'tblevents'
    def __str__(self):
        return self.name