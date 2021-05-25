from django.db import models

# Create your models here.

class History(models.Model):
    orginal_text = models.TextField()
    src = models.CharField(max_length=10)
    dest = models.CharField(max_length=10)
    translated_text = models.TextField()
    translated_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.orginal_text.split()[0] + "... - " + self.translated_text.split()[0] + "..." + "(from" + self.src + " to " + self.dest + ")"
