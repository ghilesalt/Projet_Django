from django.db import models


class User(models.Model):
    nom = models.CharField(max_length = 31)
    prenom = models.CharField(max_length = 31)
    mail = models.CharField(max_length = 51)
    mdp = models.CharField(max_length = 31)

    def __str__(self):
        return self.nom + " " + self.prenom


