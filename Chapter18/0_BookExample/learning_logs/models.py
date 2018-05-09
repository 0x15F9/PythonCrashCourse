from django.db import models

# Create your models here.
class Topic(models.Model):
    """A topic the user is learning about"""
    text = models.CharField(max_length = 200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns a string representation  of the model"""
        return self.text

class Entry(models.Model):
    """Something specific learned about a topic"""
    topic = models.ForeignKey(Topic, on_delete=models.DO_NOTHING)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "entries"

    def __str__(self):
        """Return string representation of the model"""
        t = list(self.text)
        if len(t) > 50 :
            return (t + '...')
        else:
            return self.text