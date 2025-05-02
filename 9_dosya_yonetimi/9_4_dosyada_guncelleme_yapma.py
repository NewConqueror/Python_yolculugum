# with open("newfile.txt","r+",encoding="utf-8") as dosya: # r+ hem okuma hem yazma modunda demek
#     print(dosya.read())

# with open("newfile.txt","r+",encoding="utf-8") as dosya: 
#     #dosya.write("deneme") # en baştan sığabildiği yere kadar deneme yazar üstüne yazar yani silmese de 

#     dosya.seek(17) # imleçi 17. karakterin oraya aldık
#     dosya.write("deneme") # artık 17. karakterin ordan deneme yazıcak 3 deseydim 3.karakterin ordan yazıcaktı

with open("newfile.txt","r+",encoding="utf-8") as dosya: 
    print(dosya.read())

# Sayfa Sonunda Güncelleme

# with open("newfile.txt","a",encoding="utf-8") as dosya: # r+ hem okuma hem yazma modunda demek
#     dosya.write("\nemel turan") # emel turanı dosyanın sonuna ekler a modu ile imleç sonda başlar çünkü
    

# with open("newfile.txt","r",encoding="utf-8") as dosya:
#     print(dosya.read())


# Sayfa Başında Güncelleme

# with open("newfile.txt","r+",encoding="utf-8") as dosya:
#     oku = dosya.read()
#     oku = "cemre yeni\n" + oku
#     #print(oku) # böyle gözükecek ama şuan daha dosyaya yazmadık değişkeni okuduk

#     dosya.seek(0) # imleçi başa aldık en baştan yazıyoruz yani
#     dosya.write(oku) # cemreyi de ekleyip yazdık geri kalanını üstüne yazıyoruz unutma
    

# with open("newfile.txt","r",encoding="utf-8") as dosya:
#     print(dosya.read())


# Sayfa Ortasında Güncelleme

with open("newfile.txt","r+",encoding="utf-8") as dosya:
    
    liste = dosya.readlines()
    liste.insert(1,"muhammet yeni\n")
    print(liste) # şuan bu şekilde daha dosyaya yazmadık

    dosya.seek(0)  
    # for i in liste:   # böyle for la da yazabiliriz ama bunun için bir fonksiyon var
    #     dosya.write(i) 
    dosya.writelines(liste) #direkt listeyi çevirip dosyaya yazıyor

    

with open("newfile.txt","r",encoding="utf-8") as dosya:
    print(dosya.read())