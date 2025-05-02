import pymongo

musteri = pymongo.MongoClient("mongodb+srv://new_conqueror:rCazThEcnnn4h8nr@cluster0.gixm1m8.mongodb.net/deneme?retryWrites=true&w=majority")

mydb = musteri["deneme"]

mycollection = mydb["products"]

for i in mycollection.find():
    print(i)

print("*"*50)


# update one sadece bulduğu ilk kaydı siler aynısından 2 tane varsa ilkini siler ve bırakır

mycollection.delete_one( { "ad": "redmi10 2022" } ) # birden fazla varsa ilk bulduğunu siler

mycollection.delete_many( { "ad": "redmi10 2022" } )

mycollection.delete_many( { "ad": {"#regex": "^i"} }) # adı i ile başlayan bütün kayıtları siler

sonuc = mycollection.delete_many( {} )  # {} bütün kayıtları seç demek yani bütün kayıtları siler

print(f"{sonuc.deleted_count} tane kayıt silindi")

for i in mycollection.find():
    print(i)