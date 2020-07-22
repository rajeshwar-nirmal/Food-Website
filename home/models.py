from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=12)
    Desc=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.name+" "+self.email             # this will show name of person in place of contact1,contact2......
    
