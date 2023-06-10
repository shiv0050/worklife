from django.db import models
import datetime
# Create your models here.
class Category(models.Model): # The Category table name that inherits models.Model
    name = models.CharField(max_length=30) #Like a varchar
    overhead=models.DurationField(default=datetime.timedelta())
    alloted=models.DurationField(default=datetime.timedelta())
    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")
    def __str__(self):
        return self.name #name to be shown when called

class Task(models.Model):
    name=models.CharField(max_length=30,null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default="general")
    timeStarted=models.DateTimeField(default=datetime.datetime.now(datetime.timezone.utc)+datetime.timedelta(hours=5,minutes=30))
    timeCompleted=models.DateTimeField(default=datetime.datetime.now(datetime.timezone.utc)+datetime.timedelta(hours=5,minutes=30))
    timeAlloted=models.DurationField(default=datetime.timedelta())
    overhead=models.DurationField(default=datetime.timedelta())
    class Meta:
        ordering = ["-timeStarted"] #ordering by the created field
    def __str__(self):
        return self.name #name to be shown when called
