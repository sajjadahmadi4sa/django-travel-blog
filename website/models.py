from django.db import models


class Contact (models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    class Meta :
        ordering = ['-created_date']
    
    
    def __str__(self):
        return f"{self.name} - {self.subject}"
# Create your models here.
