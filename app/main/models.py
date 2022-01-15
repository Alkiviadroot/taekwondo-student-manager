from django.db import models
from django.db.models.fields import IntegerField, TextField


class InfoMathiti(models.Model):
    onoma = models.CharField(max_length=100)
    epitheto = models.CharField(max_length=100)
    fotographia = models.ImageField(upload_to='fotografies/%Y/%m/', blank=True)
    kinito=models.IntegerField(blank=True, null=True)
    diefthinsi = models.CharField(max_length=200, blank=True)
    tk = models.IntegerField(blank=True, null=True)
    perioxi = models.CharField(max_length=100, blank=True)
    tilefonoS = models.IntegerField(blank=True, null=True)
    genethlia = models.DateField()
    enarksi = models.DateField()
    energos=models.BooleanField(default=True)
    Groups = models.TextChoices('Groups', '1 2 3 4 5 6')
    group = models.CharField(choices=Groups.choices, max_length=1, blank=True)

    def __str__(self):
        return f"{str(self.id)+'-'+self.onoma+' '+self.epitheto}"


class InfoGonios(models.Model):
    Epafi = models.TextChoices('Epafi', 'Πατέρας Μητέρα Άλλο')
    mathitis = models.ForeignKey(InfoMathiti, on_delete=models.CASCADE)
    gonios = models.CharField(choices=Epafi.choices, max_length=10)
    allo=models.CharField(max_length=100,blank=True)
    onoma = models.CharField(max_length=100)
    epitheto = models.CharField(max_length=100)
    epankelma = models.CharField(max_length=100,blank=True)
    tilefono = models.IntegerField(blank=True, null=True)
    tilefonoE = models.IntegerField(blank=True, null=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return f"{str(self.gonios)+' ('+str(self.mathitis.id)+'-'+self.mathitis.onoma+' '+self.mathitis.epitheto+')'}"


class Provlimata(models.Model):
    mathitis = models.ForeignKey(InfoMathiti, on_delete=models.CASCADE)
    kardiaka = models.BooleanField()
    kardiakaLeptomeries = TextField(blank=True)
    asthma = models.BooleanField()
    asthmaLeptomeries = TextField(blank=True)
    lipothimia = models.BooleanField()
    lipothimiaLeptomeries = TextField(blank=True)
    allo = models.BooleanField()
    alloLeptomeries = TextField(blank=True)
    date = models.DateField(auto_now=True)


    def __str__(self):
        return f"{str(self.mathitis.id)+'-'+self.mathitis.onoma+' '+self.mathitis.epitheto}"


class ProgressMathiti(models.Model):
    mathitis = models.ForeignKey(InfoMathiti, on_delete=models.CASCADE)
    epitixia = models.BooleanField()
    kup = models.DateField()
    comment = models.TextField(blank=True)
    
    

class InfoParalavi(models.Model):
    mathitis = models.ForeignKey(InfoMathiti, on_delete=models.CASCADE)
    sxesi=models.CharField(max_length=100)
    onoma = models.CharField(max_length=100)
    epitheto = models.CharField(max_length=100)
    tilefono = models.IntegerField(blank=True, null=True)


class Adies(models.Model):
    mathitis = models.ForeignKey(InfoMathiti, on_delete=models.CASCADE)
    fotografiaAdia = models.BooleanField()
    forma = models.ImageField(upload_to='forma/%Y/%m/', blank=True)

class InfoGroups(models.Model):
    Groups = models.TextChoices('Group', '1 2 3 4 5 6')
    groupNum=models.IntegerField(default=123456)
    group = models.CharField(choices=Groups.choices, max_length=1)
    Meres = models.TextChoices('Mera', 'Δευτέρα Τρίτη Τετάρτη Πέμπτη Παρασκευή Σάββατο Κυριακή')
    mera = models.CharField(choices=Meres.choices, max_length=10)
    arxi = models.TimeField()
    telos = models.TimeField()
    
class Parousiologio(models.Model):
    mathitis = models.IntegerField()
    parousia = models.BooleanField(default=False,null=True)
    date = models.DateField(auto_now=True)
    
