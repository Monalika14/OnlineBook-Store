from django.contrib import admin

# Register your models here.
from .models import Product, Rating


admin.site.register(Product)
admin.site.register(Rating)

from .models import  Contact, Orders


admin.site.register(Contact)
admin.site.register(Orders)