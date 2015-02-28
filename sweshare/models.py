from django.db import models

# Create your models here.
class Node(models.Model):
    node_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    node_text = models.CharField(max_length=3000)
    def __str__(self):
        return self.node_name