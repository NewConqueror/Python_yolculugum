# Bankamatik uygulaması 

fatihHesap = {

    "ad": "fatih",
    "hesapNo": "123456",
    "bakiye": 2000,
    "ekHesap": 1000,
}

cemreHesap = {
    "ad"     : "cemre",
    "hesapNo": "987654",
    "bakiye" : 3000,
    "ekHesap": 2000,
}

def paraCek(hesap,miktar):
    print(f"merhaba {hesap['ad']}")

    if(hesap["bakiye"]>=miktar):
        print("paranizi alabilirsiniz")
        hesap["bakiye"] -=miktar
    else:
        toplam = hesap["bakiye"] + hesap["ekHesap"]

        if(toplam>=miktar):
            ekHesapkullanimi = input("ek hesap kullanilsin mi e/h: ")

            if(ekHesapkullanimi=="e"):
                ekhesapMiktar = miktar - hesap["bakiye"]
                
                hesap["bakiye"] = 0
                hesap["ekHesap"] -= ekhesapMiktar
                print("paranizi alabilirsiniz")
            else:
                print(f"{hesap['hesapNo']} numarali hesabinizda {hesap['bakiye']} bulunmaktadir")
        else:
            print("bakiyeniz yetersiz")

paraCek(fatihHesap,2000)

def bakiyesorgula(hesap):

    print(f"{hesap['hesapNo']} numarali hesabinizda {hesap['bakiye']} TL bulunmaktadir ek hesabınızda {hesap['ekHesap']} TL bulumaktadir")
 

bakiyesorgula(fatihHesap)


