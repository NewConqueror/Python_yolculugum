import json
import os

class kullanici:
    
    def __init__(self, kullaniciadi, parola, email):
        
        self.kullaniciadi = kullaniciadi
        self.parola = parola
        self.email = email

class kullaniciyonet:
    
    def __init__(self):
        
        self.kullaniciliste = []

        self.girisYaptimi = False

        self.gecerliKullanici = {}

     #kullanicilariYukle yani kullanıcı bilgilerini json dosyası içerisinden uygulama içerisindeki listeye aticam

        self.kullanicilariYukle()

    def kullanicilariYukle(self): # listenin içerisine dosyadan okuyup aticaz bu metotla dosya okuma işlemi

        if (os.path.exists("kullanicilar.json")):

            with open("kullanicilar.json","r",encoding="utf-8") as dosya:

               kullanicilar = json.load(dosya) # dosyanın json tipindeki stringi dictionary ye çevirdik dosya için

               for kullanici in kullanicilar:
                   kullanici = json.loads(kullanici) # json stringi dictionary e çevirdik python objesine normal

                   kullanici_class = kullanici(kullaniciadi=kullanici["kullanici adi"], parola= kullanici["parola"], email=kullanici["email"])

                   self.kullaniciliste.append(kullanici_class)
            print(self.kullaniciliste)

    def kullaniciOlustur(self, yenikullanici:kullanici): # kullanici tipinde bir nesne alıcak yani yenikullanici
        
        self.kullaniciliste.append(yenikullanici) # param olarak almış olduğumuz objeyi listeye ekledik

        self.dosyaKaydet()  # yapılan son kayıtla beraber bütün listeyi tekrardan kayıt edicez dosyaya

    def girisyap(self,ad,sifre):
        
        for kullanici in self.kullaniciliste:
            if(kullanici.ad==ad and kullanici.sifre ==sifre):
                
                self.girisYaptimi = True

                self.gecerliKullanici = kullanici

                print("giris yapildi")
                break

    def cikisyap(self):
        
        self.girisYaptimi = False
        
        self.gecerliKullanici = {}


    def kimlik(self):

        if(self.girisYaptimi):
            print(f"kullanici {self.gecerliKullanici.kullaniciadi}")

    def dosyaKaydet(self):
        
        with open("kullanicilar.json","w") as dosya:

            liste = [] # aşağıda bahsettiğimiz sebeplerden dolayı tanımladık

            for yeni_kullanicim in self.kullaniciliste:
               
               liste.append(json.dumps(yeni_kullanicim.__dict__)) #class ı .__dict__ ile dict yapısına çevirdik dumpsta geri json stringe çevirdi class tipi hata verdiğinden dolayı dict e çevirmeye mecburduk yani direkt yazamazdık

            json.dump(liste, dosya) # yani kullanicliste yi okuyup başka bir listeye yazdık onu geçirdik dosyaya

            #json.dump(self.kullaniciliste, dosya) # dump dosyaya kayıt 
#                                                   dumps nesneyi kayıt edilebilir json bilgiye çeviriyordu

# burada bir problem var dump metodu kabul ettiği bazı obje tipleri var gönderebileceğimiz sınırlı yani
#  dict list tuple string int float True False None sadece bu tiptekileri alabilir ama bizimki class tipinde
# bu bilgileri ancak json alıp kayıt edilebilir json nesneye çevirebilir
# self.kullaniciliste bir class listesi bu yüzden kayıt etmek istersek bize hata vericek
# bu yüzden class bilgisini bir dict yapıya çeviricez o şekilde dump a göndericez 
#2.olarak bu bir liste her bir elemanı dolaştığımda bir class bilgisi gelicek o class bilgisini de dict yapıya çeviricez

# her class ı tek tek ulaşıp o clası dict e çeviricem ve dict e çevirdiğim veriyi ise bir liste içerisinde tutucam

yonetici = kullaniciyonet() # döngü dışında olmalı ki döngü her döndüğünde set edilmesin yeniden
#                           aynı nesneyi hedef alsın döngü her döndüğünde yonetici sıfırlanır dolayısıyla
#                           liste bilgileri yani liste içinde bulunan kullanicilar her seferinde sıfırlanır

while True:
    print('Menü'.center(50,'*'))

    secim = input('1- kullanici olustur\n2- giris yap\n3- cikis yap\n4- kimlik\n5- uygulamadan cik\nseçiminiz: ')

    if secim=="1":
        ad = input("kullanici adi: ")
        parola = input("parola: ")
        email = input("email: ")

        yenikullanici = kullanici(ad,parola,email)

        yonetici.kullaniciOlustur(yenikullanici)
        print(yonetici.kullaniciliste) # burdan da görebilirsin bir kullanici objesi döndürüyor

    elif secim=="2":
        if(yonetici.girisYaptimi):
            print("zaten giris yaptiniz")
        else:
            kad = input("kullanici adi: ")
            sifre = input("sifre: ")

            yonetici.girisyap(kad,sifre)
            
    elif secim=="3":
        yonetici.cikisyap()
    elif secim=="4":
        yonetici.kimlik()
    elif secim=="5":
        break
    else:
        print("hatali secim yaptiniz")
    