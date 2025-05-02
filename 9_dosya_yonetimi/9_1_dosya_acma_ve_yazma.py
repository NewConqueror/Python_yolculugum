""" 
Dosya Açmak ve Oluşturmak için open() fonksiyonu kullanılır
kullanımı  = open(dosyaadi,modu) mod hangi amaçla açtığımızdır

w write yazma modu yoksa oluşturur varsa içeriğini siler yazar
a append ekleme modu var olanın üstüne ekler
x create oluşturma modu dosyayı oluşturur dosya varsa hata verir
r read okuma modu dosyayı okur dosya yoksa hata verir
"""

dosya = open("belge.txt","w")
print(dosya) # dosya ile ilgili bilgileri döndürür name  mode ve encoding i

dosya.close() # dosyayı kapatır

# böyle özel konum vermezsen programın olduğu yerde oluşturur
dosya = open("C:\Users\Halime\OneDrive\Masaüstü\belge2.txt","w") 

dosya.write("fatih yeni") # dosya içine write komutu ile yazılır ama türkçe karakterler vs hata verir bunun için

dosya = open("belge.txt","w",encoding="utf-8") # bu şekilde yaparak türkçe karakter sorunu çözülür

dosya = open("belge.txt","a",encoding="utf-8") # öncekiler üstüne ekleme yapar
dosya.write("saliha yeni\n") 

dosya = open("belge.txt","x",encoding="utf-8") # dosya yoksa oluşturur varsa hata verirs