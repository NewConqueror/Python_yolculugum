# x = 10

# if x > 5:
#     raise Exception("x 5 ten büyük olamaz")  # exception mesajını fırlatmak için raise kelimemesini kullanırız


def sifrekontrol(parola): # sifrekontrol adında şifre kontrol etmek için bir fonksiyon oluşturduk

    import re # re regular expressiondan geliyo onu ekledik kontrol işlemleri için
    if (len(parola)) < 8:
        raise  Exception("şifre en az 8 karakter olmalidir")  # şifre 8 karakterden küçükse exception döndürür
    
    elif not re.search("[a-z]",parola): 
    # re.search metodu bakıyor parola değişkeninin içinde a dan z ye kadar bir karakter var mı diğerleri için de aynı
        raise Exception("şifre küçük harf içermelidir")
    
    elif not re.search("[A-Z]",parola):
        raise Exception("şifre büyük harf içermelidir")
    
    elif not re.search("[0-9]",parola):
        raise Exception("şifre bir rakam içermelidir")
    
    elif not re.search("[@_$]",parola):
        raise Exception("şifre özel karakter içermelidir")
    
    elif re.search("\s",parola):
        raise Exception("şifre boşluk içermemelidir")
    
    else:
        print("şifreniz başariyla oluşturuldu")
    
# Az önce hata veriyordu hatayı buldum " unhashable type: 'list' " hatası verdi 
# bu hata listeyi örneğin dictionary gibi kullandığında olur kullanamazsın çünkü o bir liste
# ben [] leri dışarıda unuttuğum için listeyi değiştirmeye çalışmış gibi oldum [] ler "" ın içinde olmalı

sifre = "sssadas1dasdddsaA_"

try:                     # kontrol için try except oluşturduk
    sifrekontrol(sifre)  # sifreyi gereken şartları sağlıyor mu diye kontrol etmek için yazdığımız fonk a yolladık                       raise exception hata fırlattığı için except bloğuna girecek hata çünkü
except Exception as ex:  # eğer hata verirse hangi hatayı verdiğini görmek için ex değişkeni Exception gibi davranıyor
    print(ex)            #  burda da hangi hatayı aldıysak onu yazdırıyoruz
else:
    print("geçerli parola")
finally:
    print("aşama tamamlandi")


class person:
    def __init__(self,ad,yil):
        if(len(ad)>10):
            raise Exception("isim çok uzun kisalt")
        else:
            self.ad = ad                      # class lar içinde de böyle exception lar fırlatabilirsin
        if(yil>2023):
            raise Exception("yil 2023 ten büyük olamaz")

p = person("fatii",2024)
