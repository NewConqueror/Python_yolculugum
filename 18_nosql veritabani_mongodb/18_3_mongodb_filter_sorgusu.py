import pymongo

musteri = pymongo.MongoClient("mongodb+srv://new_conqueror:rCazThEcnnn4h8nr@cluster0.gixm1m8.mongodb.net/deneme?retryWrites=true&w=majority")

mydb = musteri["deneme"]

mycollection = mydb["products"]

filtre = {"ad": "iphone12 pro max"}

sonuc = mycollection.find_one(filtre) # zaten bir taneyse böyle
print(sonuc)

sonuc = mycollection.find(filtre)  # birkaç tane olsaydı böyle vs vs


sonuc = mycollection.find_one({"_id": "64b685980ea720a03ccf3d45"})
# direkt böyle string olarak verirsen hata verir bunu object id ye çevirmemiz lazım

from bson.objectid import ObjectId 

sonuc = mycollection.find_one({"_id": ObjectId("64b685980ea720a03ccf3d45")}) # şimdi olur işte


sonuc = mycollection.find({

    "ad": {
        "$in": [ "iphone12", "redmi10" ]  # dizinin içerisindekinden 1 tanesi ad a uyuyorsa o kaydı bize getirecek
    }

})

sonuc = mycollection.find({

    "fiyat": {
        "$gt": 3000     # greater than yani fiyatı 3000 den büyük olanları bize getirir 
           
    }

})

sonuc = mycollection.find({

    "fiyat": {
        "$gte": 3000  # greater than equal yani fiyatı 3000 e eşit ve büyük olanları getirir
    }

})

sonuc = mycollection.find({

    "fiyat": {
        "$eq": 2000     # equal sadece fiyatı 2000 e eşit olanları getirir      fiyat:2000 demek ile aynı şey
    }

})

sonuc = mycollection.find({

    "fiyat": {
        "$lte": 2000     # less tah equal yani fiyatı 2000 e eşit ve daha az olanları getirir
    }

})

sonuc = mycollection.find({

    "ad": {
        "$regex": "^S" # ad alanı s ile başlayan kayıtları bize getir

#                yani regular expression da kullanabilirsin haberin olsun sadece mongodb ninkiler değil    
    }

})

for i in sonuc:
    print(i)