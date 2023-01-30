from django.db import models


# psql "postgres://avnadmin:AVNS_9HHJFR5Sm7khnm501i4@pg-b22f41e-rojina-9d3a.aivencloud.com:17169/defaultdb?sslmode=require"
class ad(models.Model):

  # id is created automatic
  description = models.CharField(max_length=300)
  email = models.CharField(max_length=100)
  state = models.CharField(max_length=50, blank=True, null=True, default='in progress')
  category = models.CharField(max_length=100, blank=True, null=True)

  def __str__(self):
    return self.id
