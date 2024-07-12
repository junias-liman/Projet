from django.db import models

# Create your models here.
class User(models.Model):
    Username=models.CharField(max_length=50)
    Lastname=models.CharField(max_length=50)
    Password=models.CharField(max_length=50)
    Identifiant=models.CharField(max_length=50)
    Mail=models.EmailField()
    Number=models.CharField(max_length=50)
    Adresse=models.CharField(max_length=50,blank=True)
    
class client(models.Model):
    Username=models.CharField(max_length=50)
    Lastname=models.CharField(max_length=50)
    Mail=models.EmailField()
    Number=models.CharField(max_length=50)
    Adresse=models.CharField(max_length=50)
    def __str__(self):
        return f"{self.Username} {self.Lastname}" 
    
class tarif(models.Model):
    nbr_vet=models.IntegerField()
    Prix=models.IntegerField()
       
class vetement(models.Model):
    libelle=models.CharField(max_length=50)
    tarif=models.ForeignKey(tarif,on_delete=models.CASCADE)
  
class images(models.Model):
    client=models.ForeignKey(client,on_delete=models.CASCADE)
    type_vetements=models.ForeignKey(vetement,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    def _str_(self):
        return self.client 

    
class depot(models.Model):
    client=models.ForeignKey(client,on_delete=models.CASCADE)
    montant=models.IntegerField()
    date_depot=models.DateField()
    date_retrait=models.DateField(blank=True, null=True)
    Regler=models.BooleanField(default=False)
    def _str_(self):
        return f"{self.montant} {self.client}" 

class depot_image(models.Model):
      depot=models.ForeignKey(depot,on_delete=models.CASCADE)
      photo=models.ForeignKey(images,on_delete=models.CASCADE)
#essai


class Item(models.Model):
    name = models.CharField(max_length=100)
    def _str_(self):
       return self.name 




class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.title




