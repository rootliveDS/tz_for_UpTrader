from django.db import models

class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=200, blank=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children')

    def __str__(self):
        return self.title