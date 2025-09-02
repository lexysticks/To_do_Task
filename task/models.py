from django.db import models

# Create your models here.
from django.utils import timezone

class Task(models.Model):

    title = models.CharField(max_length=200)                 
    description = models.TextField(blank=True, null=True)     
    completed = models.BooleanField(default=False)            
    created_at = models.DateTimeField(default=timezone.now)   
    due_date = models.DateTimeField(blank=True, null=True)    
    
    class Meta:
        ordering  =['-created_at']
    
    def __str__(self):
        return self.title
    