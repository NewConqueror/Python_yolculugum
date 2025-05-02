import pymongo

musteri = pymongo.MongoClient("mongodb+srv://new_conqueror:rCazThEcnnn4h8nr@cluster0.gixm1m8.mongodb.net/deneme?retryWrites=true&w=majority")

mydb = musteri["deneme"]

mycollection = mydb["products"]


sonuc = mycollection.find()                   # normal şekli
sonuc = mycollection.find().sort("ad")        # ad a göre sıraladık artan şekilde yani  i  r  gibi 
sonuc = mycollection.find().sort("ad",1)      # üstteki ile aynı 1 artan şekilde sırala demek
sonuc = mycollection.find().sort("ad",-1)     # ad a göre azalan şekilde sıralar r i gibi
sonuc = mycollection.find().sort("fiyat")     # fiyata göre artan şekilde
sonuc = mycollection.find().sort("fiyat", -1) # fiyata göre azalan şekilde
sonuc = mycollection.find().sort([ ("ad", 1) , ("fiyat", -1) ]) 

# önce ad a göre artan şekilde sonra fiyata göre azalan şekilde sıralar

for i in sonuc:
    print(i)