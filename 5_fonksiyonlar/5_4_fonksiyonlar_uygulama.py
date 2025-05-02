# gönderilen kelimeyi belirtilen kez yazdıran fonksiyon

def yaz(kelime,sayi):
    i=0
    while i<sayi:
        print(kelime)
        i+=1

yaz("merhaba",5)


# gönderilen sınırsız sayıdaki parametreyi listeye çeviren fonksiyon

def listecevir(*parametreler):
   liste = []

   for param in parametreler:
      liste.append(param)
        
      return liste # anlamadım niye hata veriyor
    

# mylist = listecevir(10,20,30,40,"merhaba")

# print(mylist)

# gönderilen 2 sayı arasındaki tüm asal sayıları bulan fonksiyon

def asalbul(baslangic,bitis):

    for i in range(baslangic,bitis+1):
       
       for j in range(2,i):
        
            if(i%j==0):
                break
       else:
           print(i)
            
asalbul(3,30)


#  gönderilen sayının tam bölenlerini veren fonksiyon

def bolen(sayi):
    tambolen = []
    for i in range(2,sayi):
        if(sayi%i==0):
            tambolen.append(i)   
    return tambolen       

a=bolen(20)
print(a)


