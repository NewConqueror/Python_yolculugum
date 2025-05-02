import pymongo

musteri = pymongo.MongoClient("mongodb+srv://new_conqueror:rCazThEcnnn4h8nr@cluster0.gixm1m8.mongodb.net/deneme?retryWrites=true&w=majority")

mydb = musteri["deneme"]

mycollection = mydb["products"]   

sonuc = mycollection.find_one() # ilk bulduğu kaydı bize getirir

sonuc = mycollection.find()

sonuc = mycollection.find({}, {"_id":0, "ad":1, "fiyat":1})
# bütün kayıtları getir ama sütunlardan id yi getirme ad ve fiyatı getir    1 getir 0 getirme demek

sonuc = mycollection.find({}, {"_id":0}) # bütün kayıtları getir ama id yi getirme aciklama vs bütun sütunlar gelir

sonuc = mycollection.find({}, {"_id":0, "ad":0}) # bütün kayıtları getir ama id ve ad ı getirme diğer sütunlar gelir

sonuc = mycollection.find({}, {"ad":1}) 
#sadece ad ı getir dedik ama id ile ilgili bir şey söylemediğimiz için id otomatik olarak gelir istemiyorsan id:0 de

for i in sonuc:
    print(i)


# print(sonuc)