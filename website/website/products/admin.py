from django.contrib import admin

from  .models import Category, Tovar, Delivery, Order

admin.site.register(Category)
admin.site.register(Tovar)
admin.site.register(Delivery)
admin.site.register(Order)