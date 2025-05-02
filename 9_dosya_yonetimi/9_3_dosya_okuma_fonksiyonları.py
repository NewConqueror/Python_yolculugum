# dosya = open("newfile.txt","r",encoding="utf-8")

# oku = dosya.read()

# print(oku)

# oku.close() # şimdi bu normalde yaptığımız bunu şöyle de yapabiliriz

with open("newfile.txt","r",encoding="utf-8") as dosya: # dosya olarak üzerinde işlem yap
    # yani dosya = open("newfile.txt","r",encoding="utf-8") ile aynı şey
    
    oku = dosya.read(8)
    print(oku)
    dosya.seek(9) # seek fonksiyonu imleci istediğimiz yere yerleştirmemizi sağlar 0 dersen başa 7 dersen 7.karaktere
    # 15 dersen 15. karakterin oraya yerleştirir imleci
   
    print(dosya.tell()) # tell fonksiyonu bize imlecin nerede olduğunu söyler 
    oku2 = dosya.read(8) # imlecin olduğu yerden 8 karakter okur
    print(oku2)

# with fonksiyonunu kullandığında dosyayı kapatmana gerek kalmaz o kendi kapatır