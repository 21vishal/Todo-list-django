from django.db import models

# Create your models herepython manage.py migarate app_name.
class task(models.Model):
    title=models.CharField(max_length=300)
    complete=models.BooleanField(default=False)
    createdate=models.DateTimeField(auto_now_add=True)
    
    
    
    def __str__(self):
        return self.title
    
    
