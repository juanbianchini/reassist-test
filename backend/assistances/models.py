from django.db import models
from individuals.models import Individual  

# Model Assistance
class Assistance(models.Model):
    id = models.AutoField(primary_key=True)
    individual = models.ForeignKey(Individual, on_delete=models.CASCADE, related_name="assistances")  
    date_time = models.DateTimeField(auto_now_add=True)  
    author = models.CharField(max_length=200)  
    assistance_type = models.CharField(max_length=200)  
    geolocation = models.CharField(max_length=255, blank=True, null=True) 
    details = models.TextField()  
    extended_assistance = models.BooleanField(default=False)  
    observation = models.TextField(blank=True, null=True) 

    def __str__(self):
        return f"Assistance to {self.individual.first_name} {self.individual.last_name} - {self.assistance_type} ({self.date_time})"

