from django.db import models

# Individual Model
class Individual(models.Model):
    id = models.AutoField(primary_key=True)
    dni = models.CharField(max_length=15, unique=True)  
    first_name = models.CharField(max_length=200)  
    last_name = models.CharField(max_length=200)  
    nickname = models.CharField(max_length=100, blank=True, null=True) 
    birth_date = models.DateField()  
    phone_number = models.CharField(max_length=15)  
    reference_phone_number = models.CharField(max_length=15, blank=True, null=True)  
    location = models.TextField()  # Location
    is_fixed_or_transitory_place = models.BooleanField(default=False)  
    contact_info = models.TextField(blank=True, null=True) 
    life_center = models.CharField(max_length=200, blank=True, null=True)  

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.dni})"