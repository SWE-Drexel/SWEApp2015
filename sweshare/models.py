from django.db import models

# Create your models here.
class Node(models.Model):
    node_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Edge(models.Model):
    node = models.ForeignKey(Node)
    choice_text = models.CharField(max_length=200)
    no_of_nodes = models.IntegerField(default=0)