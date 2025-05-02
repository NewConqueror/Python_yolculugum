"""
ogrenciler = {
    "120" : {
     ad ali 
     soyad yılmaz
     tel 5378965234
    }

    "125" : {
        ad can 
     soyad korkmaz
     tel 53789652687
    }

    "128" : {
        ad volkan 
     soyad yükselen
     tel 53969657687
    }

}

# 1 bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilerle dictionary içinde saklayınız

# 2 öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini gösteriniz

"""

numara = input("ogrenci numarasini giriniz: ")
ad = input("ogrencinin adini giriniz: ")
soyad = input("ogrencinin soyadini giriniz: ")
tel = input ("ogrencinin tel numarasini giriniz: ")



# ogrenciler2 = {} # bu hocanın ogrenciler ise benim

# ogrenciler2.update({
#     numara: {
#         "ad": ad,
#      "soyad": soyad,
#      "tel": tel
#     }
# })

numara2 = input("ogrenci numarasini giriniz: ")
ad2 = input("ogrencinin adini giriniz: ")
soyad2 = input("ogrencinin soyadini giriniz: ")
tel2= input ("ogrencinin tel numarasini giriniz: ")

# numara = input("ogrenci numarasini giriniz: ")
# ad = input("ogrencinin adini giriniz: ")
# soyad = input("ogrencinin soyadini giriniz: ")
# tel = input ("ogrencinin tel numarasini giriniz: ")

# ogrenciler2.update({
#     numara: {
#         "ad": ad,
#      "soyad": soyad,
#      "tel": tel
#     }
# }) 

# bizim yaptığımızda farklı değişkenler ile alıyoruz
# hocanın yaptığında ise yazıp ilerliyoruz 1.yi alıyor yazıyor sonra 2.yi ilk değişkenlerin üzerine yazıp 2.yi yazıyor

numara3= input("ogrenci numarasini giriniz: ")
ad3= input("ogrencinin adini giriniz: ")
soyad3 = input("ogrencinin soyadini giriniz: ")
tel3= input ("ogrencinin tel numarasini giriniz: ")

ogrenciler = {

numara : {
        "ad": ad,
        "soyad": soyad,
        "telefon": tel 
    },

numara2 : {
        "ad": ad2,
        "soyad": soyad2,
        "telefon": tel2 
    },

    numara3 : {
        "ad": ad3,
        "soyad": soyad3,
        "telefon": tel3 
    }

}

# numara = input("ogrenci numarasini giriniz: ")
# ad = input("ogrencinin adini giriniz: ")
# soyad = input("ogrencinin soyadini giriniz: ")
# tel = input ("ogrencinin tel numarasini giriniz: ")

# ogrenciler2[numara] = {
#     "ad": ad,
#     "soyad": soyad,
#     "tel": tel
# }

# ogrenciler2.update({
#     numara: {
#         "ad": ad,
#      "soyad": soyad,
#      "tel": tel
#     }
# })

ogrenciNo= input("görmek istediginiz ogrencinin numarasini giriniz: ")
print(ogrenciler[ogrenciNo])
# print(ogrenciler2[ogrenciNo])

# print(f"aradığınız {ogrenciNo} nolu ogrencinin ad: {ogrenciler2['ad']} soyadi: {ogrenciler2['soyad']} ve telefonu ise {ogrenciler2['tel']}")