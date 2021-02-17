from django.db import models

# Create your models here.

class stockItem(models.Model):

    def __str__(self):
        return self.stockItem

    stockCode = models.CharField(max_length=10,primary_key=True)
    stockItem = models.CharField(max_length=100)
    currentBalance = models.IntegerField()


class transaction(models.Model):

    def __str__(self):
        return (self.stockID)

    stockID = models.CharField(max_length=10)
    transDate = models.DateField()
    quantity = models.IntegerField()
    rate = models.IntegerField()
    amount = models.IntegerField()
    ops = models.CharField(max_length=8)
    stockBalanceAsOnDate = models.IntegerField()