
def not_kayitet():
    with open("sinavlar.txt","r",encoding="utf-8") as dosya:
        liste = []
        
        for i in dosya:
            print(i+" bunu yolluyoruz")
            liste.append(not_hesapla(i)) # boş listeye sırayla [fatih yeni: ] [AA] yı atadık

    with open("sonuclar.txt","w",encoding="utf-8") as dosya2:
        for i in liste:
            print(i+" listenin içinde bu var")
            dosya2.write(i)   # listenin içini dönüp yazdırdık

def not_hesapla(satir):
    satir = satir[:-1]  # 1 satır olan boşluğu sildik \n karakterini yani
    liste = satir.split(":") # fatih yeni:100,90,80 olan satırı [fatih yeni], [100,90,80] olarak 2 ye ayırdık
    ogrenciadi = liste[0]   # ogrenci adına [fatih yeni] yi 
    notlar = liste[1]       # notlara da [100,90,80] i atadık

    notlar = liste[1].split(",")  # [100,90,80] i  3 elemana böldük yani notlar = [100],[90],[80] oldu

    not1 = int(notlar[0]) # notların 0 ı yani 100
    not2 = int(notlar[1]) # 90
    not3 = int(notlar[2]) # 80

    ortalama = (not1+not2+not3)/3 # ortalamayı bulduk

    if(ortalama>=90 and ortalama<=100):  # harf notunu bulduk
        harf = "AA"
    elif(ortalama>74 and ortalama<=89):
        harf = "BA"
    elif(ortalama>49 and ortalama<=74):
        harf = "CC"
    else:
        harf = "FF"

    return ogrenciadi + ": " + harf + "\n"  # fatih yeni: AA vs diye döndürdük

def ortalama_oku():

    with open("sinavlar.txt","r",encoding="utf-8") as dosya:
        for satir in dosya:
            print(satir +"bunu yolluyoruz parçalıyoruz vs")

            print(not_hesapla(satir))  # fatih yeni: AA diye geldi yazdırdık

def not_gir():     # not girmek için bilgileri aldık
    ad = input("ad: ")
    soyad = input("soyad: ")
    not1 = input("not1: ")
    not2 = input("not2: ")
    not3 = input("not3: ")

    with open("sinavlar.txt","a",encoding="utf-8") as dosya: # aldığımız bilgileri sinavlar dosyasına ekledik
        dosya.write(ad+" "+soyad+":"+not1+","+not2+","+not3+"\n")


while True:
    islem = input("1-not gir\n2-notları oku\n3-kayıt et\n4-çıkış\nseciminiz: ")

    if(islem=="1"):
        not_gir()
    elif(islem=="2"):
        ortalama_oku()
    elif(islem=="3"):
        not_kayitet()
    else:
        break