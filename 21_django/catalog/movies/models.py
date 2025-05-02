from django.db import models

# Create your models here.

class film(models.Model):

    # verbose name ile daha önce eklemiş olduğumuz alanlardaki yazıları değiştirdik
    ad = models.CharField(max_length=100, verbose_name="Filmin adı ")
    aciklama = models.TextField(verbose_name="Filmin aciklamasi")
    resim = models.CharField(max_length=50, verbose_name="Filmin resmi")
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True, verbose_name="eklenme tarihi")
    yayinlandimi = models.BooleanField(default= True) 
    
    #ad = models.CharField(max_length=100)   # django yönetim panelinde film adı için max 100 kelimelik alan ekledik
    # aciklama = models.TextField()          # django yönetim panelinde film aciklamasi için alan ekledik
    # resim = models.CharField(max_length=50)# django yönetim panelinde film resmi için max 50 kelimelik alan ekledik
    # olusturma_tarihi = models.DateTimeField(auto_now_add=True)
    # o anki tarih neyse onu olusturulma tarihi olarak verdik

    def __str__(self):
        return self.ad 
        # return self.olusturma_tarihi eğer böyle yaparsan ot i gözükür
# bunu yazınca django yönetim panelinde filme tıkladığın zaman adları gözükür
    def get_image_path(self): # resim yolu için fonksiyon yazdık
        return "/img/"+ self.image
