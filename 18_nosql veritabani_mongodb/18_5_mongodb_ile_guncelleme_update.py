import pymongo

musteri = pymongo.MongoClient("mongodb+srv://new_conqueror:rCazThEcnnn4h8nr@cluster0.gixm1m8.mongodb.net/deneme?retryWrites=true&w=majority")

mydb = musteri["deneme"]

mycollection = mydb["products"]

for i in mycollection.find():
    print(i)

# update one sadece bulduğu ilk kaydı günceller aynısından 2 tane varsa ilkini günceller ve bırakır
mycollection.update_one(
    
    { "ad": "iphone12"},
    { "$set":{
        "ad":"iphone13",
        "fiyat": 5000  # aynı anda birden fazla alanı da güncelleyebilirsin
    }}
)

for i in mycollection.find():
    print(i)

# update many bulduğu bütün kayıtları günceller 3 5 kaç tane olduğu fark etmez
mycollection.update_many(
    
    { "ad": "redmi10"},  
    { "$set":{
        "ad":"redmi10 2022",
        "fiyat": 5000  
    }}
)

for i in mycollection.find():
    print(i)


sorgulama = { "ad": "redmi10"}

yenidegerler = { "$set":{
        "ad":"redmi10 2023",
        "fiyat": 5000  
    }}

sonuc = mycollection.update_many(sorgulama, yenidegerler)

print(f"{sonuc.modified_count} tane kayıt güncellendi")

for i in mycollection.find():
    print(i)