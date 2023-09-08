from django.db import models


class Administratif(models.Model):
    nom = models.CharField(max_length=250)
    prenom = models.CharField(max_length=250, default="")
    email = models.EmailField(max_length=250, default="")
    tel = models.IntegerField(default="")
    annEmploi = models.IntegerField(default="")

    def __str__(self):
        return self.nom
# ***********************model pour annee academique*********************

class Annee(models.Model):
    annee_acad = models.CharField(max_length=250)

    def __str__(self):
        return self.annee_acad
# *******************model pour deparetement*****************

class Departement(models.Model):
    nom_departement = models.CharField(max_length=250)

    def __str__(self):
        return self.nom_departement
# ***********model pour departement***************

class Filiere(models.Model):
    nom_filiere = models.CharField(max_length=250)
    ID_Departement = models.ForeignKey(Departement, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom_filiere
# ***********model pour niveau***********
class Niveau(models.Model):
    Nom_niveau = models.CharField(max_length=250)

    def __str__(self):
        return self.Nom_niveau
# *************************model pour clase**************
class Classe(models.Model):
    nom_classe = models.CharField(max_length=250)
    ID_Filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE)
    ID_niveau = models.ForeignKey(Niveau, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom_classe
# *******model pour modul******
class Modul(models.Model):
    nom_modul = models.CharField(max_length=250)
    ID_Classe = models.ForeignKey(Classe, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom_modul
# ********model pour Etudiant*******
class Etudiant(models.Model):
    nom = models.CharField(max_length=250)
    prenom = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    tel = models.CharField(max_length=250)
    annEntre = models.CharField(max_length=250)
    ID_Annee = models.ForeignKey(Annee, on_delete=models.CASCADE)
    ID_Classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
    ID_Modul = models.ForeignKey(Modul, on_delete=models.CASCADE)

    def __str__(self):
       return self.nom