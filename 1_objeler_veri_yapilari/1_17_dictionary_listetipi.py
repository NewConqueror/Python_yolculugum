# bu liste tipi  key - value şeklinde çalışıyor yani anahtar - değer yani değere ulaşmak için bir anahtar kullanıyoruz

# 41 => kocaeli  34 => istanbul gibi 

sehirler = ["kocaeli","istanbul"]
plakalar = [41,34]

print(plakalar[sehirler.index("kocaeli")]) # dictionary olmadan böyle yaparız ama gördüğün gibi bu amele işi
# bir de hepsi sıralı olmalı ki index değerleri denk gelebilsin

# print(plakalar["kocaeli"]) => 41
# print(plakalar["istanbul"]) => 34  direkt bu değerlere götürmeli mesela

# plakalar = {"key" : "value"} bu şekilde çalışır

plakalar = { "kocaeli" : 41 , "istanbul" : 34} 

print(plakalar["kocaeli"])
print(plakalar["istanbul"]) # direkt bize sonucu verirler

plakalar["ankara"] = 6 #dedik ankara değeri olmadığı için direkt aticak sadece değiştirmek için değil yani
plakalar["kocaeli"] = "new value"

print(plakalar)

# users = {
#     "fatih yeni" : 18, sadece böyle olmak zorunda değil bunun içinde de parantez açabiliriz
#     "saliha yeni" :12
# }


users = {
    "fatih yeni" : {
        "yas" : 18,
        "email": "fatihyeni999@gmail.com",
        "roller": ["admin","user"], # böyle bir şey de yapabiliriz sıkıntı çıkarmaz
        "adres": "cirpici",
        "telefon": "5555555555"
    },
    "saliha yeni" : {
        "yas" : 12,
        "email": "salihayeni999@gmail.com",
        "roller": ["user"],
        "adres": "cirpici",
        "telefon": "5555555555"
    }
}

print(users["fatih yeni"]) # dediğimizde fatih yeni nin bütün bilgisi gelicek

print(users["fatih yeni"]["yas"]) 
print(users["fatih yeni"]["email"])  # bu şekilde sadece istediğimiz yere de ulaşabiliriz
print(users["fatih yeni"]["adres"]) 

print(users["fatih yeni"]["roller"][0]) # admin gelicek burda mesela