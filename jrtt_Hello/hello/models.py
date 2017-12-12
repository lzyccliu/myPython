from django.db import models

# Create your models here.

class Owner(models.Model):
    GENDER = (
        ('M','MALE'),
        ('F','FEMALE')
    )
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, unique=True)
    gender = models.CharField(max_length=1, choices=GENDER)
    birthday = models.DateField()

    def __str__(self):
        return f'Owner(id:{self.id},name:{self.name},gender:{self.gender},birthday:{self.birthday}'
class Pet(models.Model):
    TYPE = (
        ('C','Cat'),
        ('D','Dog'),
        ('H','Human')
    )
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=1,choices=TYPE)

    def __str__(self):
        return f'Pet(id:{self.id},name:{self.name},type:{self.type}'