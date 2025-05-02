from django.contrib import admin
from .models import film
# Register your models here.

#admin.site.register(film)

class filmadmin(admin.ModelAdmin):
    list_display = ("id","ad","olusturulma_tarihi","yayinlandimi")
    list_display_links =("id","ad")
    list_filter = ("olusturulma_tarihi",)
    list_editable = ("yayinlandimi",) # checkbox koyar bildiğin 
    search_fields = ("ad","aciklama") # arama özelliği gelir
    list_per_page = 20 # bir sayfada kaç tane kayıt olsun

admin.site.register(film, filmadmin)