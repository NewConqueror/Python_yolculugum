# range(başlangıç,bitiş,artış miktarı)

for item in range(10): # 0 dan 10 a kadar birer artarak yazar
    print(item) 

for item in range(50,100,10): # 50 den başlayıp 100 e kadar onar artarak yazar
    print(item)     

print(list(range(50,100,10))) # 50 den başlayıp 100 e kadar onar artarak listeye yazar list ile listeye çevirirsin


# enumerate  indeksi görmek istiyorum ama ayrıca index diye bir şey tanımlamicam

greeting = "hello there"

index = 0

for letter in greeting:
    print(f"index: {index} letter: {letter} veya letter: {greeting[index]}")
    index+=1

for item in enumerate(greeting):
    print(item)

for index,item in enumerate(greeting):
    print(f"index: {index} letter: {item}")
            

# zip  iki listeyi birbirleriyle eşleştirme yapar dictionary gibi ama fonksiyon 

list1 = [1,2,3,4,5]
list2 = ["a","b","c","d","e"]
list3 = [100,200,300,400,500]
print(list(zip(list1,list2,list3))) # index mantığı hepsinin 0 ı birbirleriyle eşleşir

for item in zip(list1,list2,list3):
    print(item)

for a,b,c in zip(list1,list2,list3):
    print(a,b,c)    