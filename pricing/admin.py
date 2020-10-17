from django.contrib import admin
from .models import Pricing,Photography,Photos,Processing,TypeOfCamera,Resolution,Term

# Register your models here.
admin.site.register(Pricing)
admin.site.register(Photography)
admin.site.register(Photos)
admin.site.register(Processing)
admin.site.register(TypeOfCamera)
admin.site.register(Resolution)
admin.site.register(Term)
