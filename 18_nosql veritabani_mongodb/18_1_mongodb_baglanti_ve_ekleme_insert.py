import pymongo

musteri = pymongo.MongoClient("mongodb+srv://new_conqueror:rCazThEcnnn4h8nr@cluster0.gixm1m8.mongodb.net/deneme?retryWrites=true&w=majority")

mydb = musteri["deneme"]

print(musteri.list_database_names()) # serverdaki database leri yazdırır

mycollection = mydb["products"]   # varsa bağlanır yoksa oluşturur

print(mydb.list_collection_names) # collention ları yazdırır

product = {"ad": "redmi10", "fiyat":3000}

sonuc = mycollection.insert_one(product) # bir tane kayıt yapacaksak insert one kullanırız

print(sonuc)        # bir obje olduğunu görmüş olduk
print(type(sonuc))  # class tipinde olduğunu gördük
print(sonuc.inserted_id) # mongodb nin otomatik verdiği id yi görürüz

productlist = [
    {"ad": "redmi10 pro", "fiyat":4000},
    {"ad": "iphone12", "fiyat":10000},
    {"ad": "iphone12 pro", "fiyat":11000},
    {"ad": "iphone12 pro max", "fiyat":12000}
]
 
# productlist2 = [                                 # id yi bu şekilde kendimiz de verebiliriz
#     {"_id":1 ,"ad": "redmi10 pro", "fiyat":4000},
#     {"_id":2 ,"ad": "iphone12", "fiyat":10000},
#     {"_id":3 ,"ad": "iphone12 pro", "fiyat":11000},
#     {"_id":4 ,"ad": "iphone12 pro max", "fiyat":12000}
# ]

# illa verilerin aynı olması gerekmiyor birini eklerim birine eklemem paşa gönlüm öyle istiyor

productlist = [
    {"ad": "redmi10 pro", "fiyat":4000, "aciklama":"iyi telefon"},
    {"ad": "iphone12", "fiyat":10000, "kategoriler": ["telefon","elektronik"] },
]

sonuc = mycollection.insert_many(productlist)
print(sonuc.inserted_ids)  # bu sefer ids çünkü çoğul anladın hepsinin id si liste şeklinde yazdırılır