ad = "fatih"
soyad = "yeni"
yas = 18

selamlama = "merhaba ben: "+ad + " "+soyad + " ve ben \n"+ str(yas) +" yasindayim." 
print(selamlama)

uzunluk = len(selamlama)
print(uzunluk)
print(selamlama[0])  # ilk karakter
print(selamlama[uzunluk-1]) # son karakter
print(selamlama[-1]) # yukarıdak ile aynı işi yapar
print(selamlama[2:6]) # 2.indisten 6.indise kadar yaz 6. indis dahil değil 2,3,4 ve 5 i yazacak yani rhab yazacak
print(selamlama[2:]) # 2.indisten sona kadar yazacak
print(selamlama[:18]) # en baştan yani 18 e kadar 18 dahil değil yani 0.indisten 17.indise kadar yazar
print(selamlama[0:uzunluk:2]) # 0 dan sona kadar her iki indiste bir yazıcak yani 0 2 4 6 8 ... indisleri yazacak