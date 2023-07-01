from django.db import models

# Create your models here.
class employe(models.Model):
    eid=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=15)
    age=models.IntegerField()
    mobile=models.CharField(max_length=15,unique=True)
    email=models.EmailField(max_length=75,unique=True)
    city=models.CharField(max_length=25)
    salary=models.FloatField()

class Meta:
    db_table="empdata"