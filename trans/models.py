from django.db import models

# Create your models here.

class History(models.Model):
    orginal_text = models.TextField()
    src = models.CharField(max_length=10)
    dest = models.CharField(max_length=10)
    translated_text = models.TextField()

    def __str__(self):
        title = self.orign_text.split()[:2] + "... - "
        title += self.translated_text.split()[:2] + "..."
        title += "( from" + self.src + " to " + self.dest + ")"
        return title