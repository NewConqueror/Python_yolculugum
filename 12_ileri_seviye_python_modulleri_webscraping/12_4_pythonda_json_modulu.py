# dictionary

person = {"name: ":"fatih","languages":["python","C#"]}

sonuc = person["name: "]
sonuc = person["languages"]
sonuc = person["languages"][0] # dictionary yani sözlük yapısını hatırlamış olduk json yapısı buna benziyor

import json 

person_string = '{"name: ":"fatih","languages":["python","C#"]}' # dict in stringe çevirilmiş hali

# şimdi bu string yapıyı yani json yapısını dictionary ye çeviricez

sonuc = json.loads(person_string)  # loads metoduna bir tane json stringi gönderdiğimiz zaman bunu
#                                    dictionary e çevirmiş oluruz
print(type(sonuc)) # bu da dict olduğunun kanıtı
 
sonuc = sonuc["name"]       # artık dict olduğu için bu şekilde erişebiliriz
sonuc = sonuc["languages"]


# dosyadan json bilgiyi bu şekilde okuyabiliriz

with open("person.json") as dosya:
    
    data = json.load(dosya) # dosyanın json tipindeki stringi dictionary ye çevirdik
    print(data["name"])
    print(data["languages"])



person_dict = {
    "name":"fatih",
    "languages":["python","C#"]
}


sonuc = json.dumps(person_dict) # burda da dict bir nesneyi json stringine çevirdik
# print(sonuc["name"])          # artık bu bilgiye ulaşamayız hata verir çünkü bir json stringi


# dosyaya json bilgiyi bu şekilde yazabiliriz

with open("person.json","w") as dosya:
    json.dump(person_dict,dosya)        # dict nesnesini  json stringine çevirip dosyaya yazdık


person_dict = json.dumps(person_string) # json stringi dict e çevirdik 
print(person_dict) # diyelim ki ben bunu daha okunaklı boşluklu yazdırmak istiyorum nasıl yapıcam bunu


person_dict = json.dumps(person_string, indent=4, sort_keys=True) # indent ile boşluk bıraktık sort_keys ile de
#                                                                 key leri alfabeye göre sıraladık

print(person_dict) # bu sefer daha okunaklı daha düzgün yazar