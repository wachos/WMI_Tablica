from django.db import models
from django.forms import ModelForm
# Create your models here.
class Ogloszenie(models.Model):
    Kategoria1 = 'K1'
    Kategoria2 = 'K2'
    Kategoria3 = 'K3'
    Kategoria4 = 'K4'
    KATEGORIE_CHOICES = (
        (Kategoria1, 'Kategoria1'),
        (Kategoria2, 'Kategoria2'),
        (Kategoria3, 'Kategoria3'),
        (Kategoria4, 'Kategoria4'),
    )
    kategoria = models.CharField(max_length=2,
                                      choices=KATEGORIE_CHOICES,
                                      default=Kategoria1)
	
    data_publikacji = models.DateField()
    tytul = models.CharField(max_length=200)
    tresc = models.TextField(max_length=500)
    photo = models.ImageField(upload_to='cars')

class OgloszenieForm(ModelForm):
	class Meta:
		model = Ogloszenie
