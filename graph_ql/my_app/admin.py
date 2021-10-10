from django.contrib import admin


from .models import Store,Item,Invoice
# Register your models here.
admin.site.register(Store)
admin.site.register(Item)
admin.site.register(Invoice)
