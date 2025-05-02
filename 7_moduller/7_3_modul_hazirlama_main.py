import ders52_modul_hazirlama # type: ignore

"""
ders52_modül_hazirlama yi kendim yapmiştim python dersleri klasörünün içindeydi 
sonra onu ordan alip python un genel kütüphanesi olan "lib" in içine attim 
program ayni şekilde herhangi bir hata vermeden çalişti modül ile ana program illa ayni 
klasör içinde olmak zorunda değil yani

"""

# sonuc = help(ders52_modül_hazırlama)
# sonuc = help(ders52_modül_hazırlama.fonksiyon)

sonuc = ders52_modul_hazirlama.number
print(sonuc)

sonuc = ders52_modul_hazirlama.numbers
print(sonuc)

# sonuc = ders52_modül_hazırlama.person["ad"]  # yazılabilir değil diyor anlamadım
# print(sonuc)

# sonuc = ders52_modül_hazırlama.person["yas"]
# print(sonuc)

sonuc = ders52_modul_hazirlama.fonksiyon(10)
print(sonuc)


p = ders52_modul_hazirlama.person()

p.konus()





