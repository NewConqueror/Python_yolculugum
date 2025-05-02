def benim_decoratorum(fonksiyon):
    
    def içtekifonk():
        print("fonksiyondan önceki işlemler")
        fonksiyon()
        print("fonksiyondan sonraki işlemler")

    return içtekifonk


# def merhaba():
#     print("merhaba")

# def selam():
#     print("selam")

# merhaba = benim_decoratorum(merhaba) # artık merhaba fonksiyonu döndürdüğümüz içteki fonksiyon ile aynı oldu
# #                                     bir daha benim_decoratörümü çağırmaya gerek yok 
# # artık merhaba() fonksiyonu aslında = benim_decoratorum(merhaba) anlamına geliyor 

# merhaba() # fonksiyonun kendisiyle beraber decorator fonksiyon da çalıştı

# selam = benim_decoratorum(selam) # yukarıdaki işlemin aynısı 
# selam() 
# #       bunu bu şekilde yapmak zorunda değiliz şöyle yapabiliriz

# @benim_decoratorum
# def merhaba():
#     print("merhaba")

# merhaba()

 # eğer böyle parametre verirsek yukarıdakini de düzeltmeliyiz
# @benim_decoratorum
# def merhaba(ad):
#     print("merhaba ",ad)

# merhaba("fatih")


def benim_decoratorum(fonksiyon):
    
    def içtekifonk(ad):
        print("fonksiyondan önceki işlemler")
        fonksiyon(ad)
        print("fonksiyondan sonraki işlemler")

    return içtekifonk

@benim_decoratorum
def merhaba(ad):
    print("merhaba ",ad)

merhaba("fatih")

# şimdi daha somut bir örnek yapalım

import math
import time # işlemin ne kadar sürede tamamlandığını öğrenmek isteyen biriyim diyelim

# def usal(a,b):

#     baslangic = time.time()

#     time.sleep(1)

#     print(math.pow(a,b))

#     bitis = time.time()

#     print("fonksiyon " + str(bitis-baslangic) +" saniye sürdü")

# def faktoriyel(sayi):

#     baslangic = time.time()

#     time.sleep(1)

#     print(math.factorial(sayi))

#     bitis = time.time()

#     print("fonksiyon " + str(bitis-baslangic) +" saniye sürdü")

# usal(2,3)
# faktoriyel(5)

# ÖNEMLİ
#  aga 100 tane fonk olsa hepsinde zamanı aynı şeyleri yazarak mı hesaplicam olmaz buna bir çözüm bulmak lazım
#  bu fonksiyonlar çalıştığında onlarla birlikte zamanı hesaplayan fonksiyonun da çalışması lazım
#  bunu da ya o fonksiyonu hepsinde çağırıcam kod olarak ya da decorator ile otomatik çağırılacak
#  decorator kullanmak çok daha mantıklı


def zaman_hesapla(fonksiyon):

    def içtekifonksiyon(*args,**kwargs): # 1 2 değil istediğimiz sayıda parametre verebilmemiz için böyle dedik

        baslangic = time.time()

        time.sleep(1)

        fonksiyon(*args,**kwargs) # 1 2 değil istediğimiz sayıda parametre verebilmemiz için args kwargs kullandık

        bitis = time.time()

        print("fonksiyon " +fonksiyon.__name__+" "+ str(bitis-baslangic) +" saniye sürdü")
    
    return içtekifonksiyon

@zaman_hesapla # zaman_hesapla(usal(a,b)) gibi düşünebilirsin
def usal(a,b):

    print(math.pow(a,b))

    
@zaman_hesapla
def faktoriyel(sayi):

    print(math.factorial(sayi))


@zaman_hesapla
def toplama(a,b):
    print(a+b)


usal(2,3)    # fonksiyonlar çalıştıkları zaman onlarla birlikte zaman hesapla decorator ındaki fonksiyon da çalışıyor
faktoriyel(5)# böylece fazladan kod yazmaya gerek kalmadan otomatik olarak hallediyoruz
toplama(5,2)