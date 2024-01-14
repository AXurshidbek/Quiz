from django.db import models

class Soha(models.Model):
    nom=models.CharField(max_length=25)


class Savol(models.Model):
    matn=models.TextField()


class Variant(models.Model):
    matn=models.TextField()
    savol=models.ForeignKey(Savol, on_delete=models.CASCADE)
    togri=models.BooleanField()




class Yuborish(models.Model):
    savol = models.ForeignKey(Savol, on_delete=models.CASCADE)
    soha = models.ForeignKey(Soha, on_delete=models.CASCADE)