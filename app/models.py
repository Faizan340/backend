from django.db import models

class Contact(models.Model):
    """
    Mapped with Contact from SFDC
    """
    #Title = models.CharField(choices=TITLE_CHOICES, max_length=9, blank=False, null=False)
    FirstName = models.CharField(max_length=255, blank=True, null=True)
    LastName = models.CharField(max_length=255, blank=False, null=False)
    Email = models.CharField(max_length=255, blank=False, null=False, unique=True)
    Phone = models.CharField(max_length=255, blank=False, null=False, unique=True)

    def __str__(self):
        return self.FirstName

class Classname(models.Model):
    Name = models.CharField(max_length=50, blank=False, null=False)

def __str__(self):
    return self.Name
