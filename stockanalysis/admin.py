from django.contrib import admin
from . models import Stock,StockData
# Register your models here.

class StockAdmin(admin.ModelAdmin):
    search_fields = ('id','Name','Symbol')

admin.site.register(Stock,StockAdmin)
admin.site.register(StockData)