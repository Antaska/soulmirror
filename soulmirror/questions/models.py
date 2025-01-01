from django.db import models

# Create your models here.
class Question(models.Model):
    id = models.AutoField(primary_key=True)
    tematica = models.CharField(max_length=50)
    pregunta = models.TextField()
    respondida = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.id}. [{self.tematica}] {self.pregunta}"