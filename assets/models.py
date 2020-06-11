from django.db import models

class Asset(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    file = models.FileField(upload_to='assets/')
    dateadded = models.DateField(auto_now=True)
    QUARANTINE = 'Quarantine'
    STIGMA = 'Stigma'
    TESTING = 'Testing'
    category_choices = [
        (QUARANTINE,'Quarantine related'),
        (STIGMA,'Stigma related'),
        (TESTING,'Testing related'),
    ]
    category = models.CharField(max_length=200, choices=category_choices, default=STIGMA)

    def __str__(self):
        return self.title

    def get_quarantine(self):
        if self.category = QUARANTINE
            return self
        else:
            pass

    def get_stigma(self):
        if self.category = STIGMA
            return self
        else:
            pass

    def get_testing(self):
        if self.category = TESTING
            return self
        else:
            pass