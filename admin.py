from django.contrib import admin
from .models import stockItem,transaction

# Register your models here.
admin.site.register(stockItem)
admin.site.register(transaction)