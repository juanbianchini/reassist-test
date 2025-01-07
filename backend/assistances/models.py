from django.db import models
from individuals.models import Individual  

# Model Assistance
class Assistance(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="id")
    individual = models.ForeignKey(Individual, on_delete=models.CASCADE, related_name="assistances")  
    date_time = models.DateTimeField(auto_now_add=True, verbose_name="date and time")  
    author = models.CharField(max_length=100, verbose_name="author")  
    assistance_type = models.CharField(max_length=100, verbose_name="assistance type")  
    geolocation = models.CharField(max_length=255, blank=True, null=True, verbose_name="geolocation") 
    details = models.TextField(blank=True, null=True, verbose_name="details")  
    extended_assistance = models.BooleanField(default=False, verbose_name="follow-up needed")  
    observation = models.TextField(blank=True, null=True, verbose_name="observation")    

    def __str__(self):
        return f"ASSISTANCE: {self.individual.name} {self.individual.surname} - {self.assistance_type} ({self.date_time})"

