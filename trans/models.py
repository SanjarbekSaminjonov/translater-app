from django.db import models

# Create your models here.

class History(models.Model):
    orign_text = models.TextField()
    src = models.CharField(max_length=10)
    dest = models.CharField(max_length=10)
    translated_text = models.TextField()

    def __str__(self):
        return self.orign_text.split()[0] + "... - " + self.translated_text.split()[0] + "..." + "(from " + self.src + " to " + self.dest + ")"
