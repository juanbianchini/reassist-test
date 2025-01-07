from django.db import models
from django.core.validators import RegexValidator

# Individual Model
class Individual(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="id")
    dni = models.CharField(max_length=8, blank=True, unique=True, null=True, verbose_name="dni", validators=[RegexValidator(
            regex=r'^\d{8}$', 
            message='DNI must be an 8-digit number'
        )])  
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name="name")  
    surname = models.CharField(max_length=100, blank=True, null=True, verbose_name="surname")  
    nickname = models.CharField(max_length=100, blank=True, null=True, verbose_name="nickname") 
    birth_date = models.DateField(help_text ="Please use the following format: <em>YYYY-MM-DD</em>.", null=True, verbose_name="birth date")  
    phone_number = models.CharField(max_length=15, null=True, blank=True, verbose_name="phone")  
    reference_phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name="reference phone")  
    location = models.TextField(null=True, blank=True, verbose_name="location")  
    is_fixed_or_transitory_place = models.BooleanField(default=False, verbose_name="transitory location")  
    contact_info = models.TextField(blank=True, null=True, verbose_name="contact info") 
    life_center = models.CharField(max_length=100, blank=True, null=True, verbose_name="life center")  

    def __str__(self):
        return f"{self.name} {self.surname} ({self.dni})"