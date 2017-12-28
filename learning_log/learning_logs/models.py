from django.db import models
# Create your models here.
from tinymce.widgets import TinyMCE

class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class Entry(models.Model):
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    text = models.TextField(widget=TinyMCE(attrs={'cols':80,'rows':30}))
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        t = len(self.text)
        if t<50:
            return self.text
        else:
            return self.text[:50] + "..."
