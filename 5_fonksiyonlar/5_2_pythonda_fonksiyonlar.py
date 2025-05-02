def sayhello(name = "user"): # def define dan geliyor tanımlamak yani sonra klasik fonk adı parametresi vs
    print("hello "+name)     # default olarak user ı atadık parametresiz de hello user yazıcak

sayhello("fatih")
sayhello("cemre")
sayhello()


def sayhello(name = "user"): # def define dan geliyor tanımlamak yani sonra klasik fonk adı parametresi vs
     return   "hello "+ name # dönüş değerini senin vermen gerekmiyor otomatik olarak anlıyor sen sadece
                             # normal return diyorsun kalanını o hallediyor
msg = sayhello("fatih")
msj = sayhello("cemre")
msgg=sayhello()

def topla(sayi1,sayi2):
     return sayi1+sayi2

sonuc = topla(10,20)
print(sonuc)


def yashesapla(dogumYili):
     return 2023 - dogumYili

yasFatih = yashesapla(2004)
yassaliha= yashesapla(2012)

print(yasFatih,yassaliha)


def emekliligeKacYilkaldi(dogumyili,isim):
     """
     DOCSTRİNG: dogum yiliniza gore emekliliginize kac yil kaldi
     INPUT: dogum yili
     OUTPUT:  hesaplanan emekli olma yasi
     """

     yas = yashesapla(dogumyili)
     emeklilik = 65 - yas

     if(emeklilik>0):
          print(f"emekli olmaniza {emeklilik} yil kaldi")
     else:
          print("zaten emekli oldunuz.") 


emekliligeKacYilkaldi(2004,"fatih")
emekliligeKacYilkaldi(1971,"yasar")         

print(help(emekliligeKacYilkaldi)) # help metodu sana fonksiyonu nasıl kullanacağını ne işe yaradığını gösterir 


print(help(list.append))  # append metodunun ne işe yaradığını nasıl kullanılacağını bize gösterir
