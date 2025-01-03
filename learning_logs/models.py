from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Topic (models.Model) :
    '''a topic  the user is learning about.'''
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def _str_ (self):
        """:returning a string representation of the model ."""
        return self.text

class Entry(models.Model):
    """something specific learned about a topic."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta :
        verbose_name_plural = 'entries'

    def _str_(self):
        ''':returning a simple string represnting the entry. '''
        return f"{self.text[:50]}..."
