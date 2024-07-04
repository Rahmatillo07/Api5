from django.db import models


class Zone(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        unique_together = ['name']

    def __str__(self):
        return self.name


class Institution(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date_created = models.DateField()
    zone = models.ForeignKey(Zone,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Building(models.Model):
    institution = models.ForeignKey(Institution,on_delete=models.CASCADE)
    zone = models.ForeignKey(Zone,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    area = models.CharField(max_length=20)
    floor = models.CharField(max_length=10)
    accommodation = models.BooleanField()
    playground = models.BooleanField()
    lift = models.BooleanField()

    def __str__(self):
        return self.name



