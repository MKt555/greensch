from django.db import models

#Models for main page

class News (models.Model):
    """Highlights and Information about school and its work."""
    Title = models.CharField(max_length=100, blank = True, null = True, unique = True)
    Content = models.TextField()

