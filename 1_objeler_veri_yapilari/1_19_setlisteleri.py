meyveler = {"muz","elma","portakal"} # böyle süslü parantez içinde tanımlarsan set listesi olmuş oluyor ne garip

print(meyveler)  # bu normal bir şekilde çalışır
# print(meyveler[0]) # index bilgisi ile ulaşamazsın hata verir set listeleri indekslenemezdir

for x in meyveler:
    print(x) # set listeleri indekslenemediği için sıralanamaz da rastgele verir değerleri
    # ilk çalıştırdığımda muz,portakal,elma şeklindeydi 2. çalıştırdığımda elma,muz,portakal şeklinde
    # set listelerinde bir şeyi sıralayamazsın yani

meyveler.add("kiraz") # bu şekilde de ekleyebilirsin ama sıra olmadığı için nere ekleyeceğini bilemezsin unutma
meyveler.update(["mango","üzüm"]) # bu şekilde update içine bir liste gönderebilirsin
meyveler.update(["armut","ceviz","elma"]) # elma zaten liste içerisinde olduğu için bir daha eklemicek
# set listelerinde bir elemandan sadece bir tane olabilir

meyveler.add("kiraz")
meyveler.add("muz") # bu da kanıtı

# unutma set listelerinde index diye bir şey olmadığı için her yere eklenebilir eklediğin şey baş son orta vs
# {'üzüm', 'portakal', 'muz', 'elma', 'kiraz', 'mango'} çıktıyı bu şekilde verdi hesap et işte
print(meyveler)

mylist = [1,2,5,4,4,2,1]
print(mylist)
print(set(mylist)) # bize içeride tekrar edenleri silip sadece [1,2,4,5] değerlerini gösterecek ve sıralıyor bu da +

meyveler.remove("mango") # remove aynen çalışır
meyveler.discard("elma") # ek olarak discard diye bir fonksiyon var aynı işi yapar remove ile

print(meyveler)
meyveler.pop() # normalde bu şekilde çalıştırıldığında son elemanı siler
# ama set listelerinde index diye bir şey olmadığından rastgele bir elemanı siler

meyveler.clear() # aynı işe yarar bütün elemanları siler