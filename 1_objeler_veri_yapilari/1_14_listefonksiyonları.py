numbers = [1,10,5,16,4,9,10]
letters = ["a","g","s","b","y","a","z"]

val = min(numbers) # diziyi tarar ve minimum değeri bulur
print(val)
val=max(numbers) # diziyi tarar ve  maksimum değeri bulur
print(val)

val = max(letters) # diziyi tarar ve  maksimum değeri bulur
print(val)
val = min(letters) # diziyi tarar ve minimum değeri bulur
print(val)

val = numbers[3:6] # 3.indisten 6.indise kadar alır
print(val)

val = numbers[:3]
print(val)

val = numbers[4:]
print(val)

numbers[4] = 40 # stringteki gibi aynı bu şekilde değerini değiştirebilirsin

numbers.append(49) # dizinin sonuna eleman ekler int şart değil "49" yazsan string olarak eklerdi
numbers.append(59)

numbers.insert(3, 78) # nereye neyi  3.indise 78 değerini ekler

numbers.insert(-1 ,52) # kendisine yer açtığı için sona değil sondan 1 öncekine yazılmış olur

numbers.pop() # sondaki elemanı döndürür ve siler 
numbers.pop(-1) # yukarıdaki ile aynı işi yapar sondaki elemanı döndürür ve siler

numbers.pop(0) # ilk elemanı döndürür ve siler

numbers.remove(49) # dizinin içinden 49 değerini bulur ve siler


numbers.sort() # diziyi  küçükten büyüğe doğru sıralar
numbers.reverse() # diziyi ters çevirir az önce küçükten büyüğe sıralamıştık artık büyükten küçüğe oldu

letters.sort() # diziyi  küçükten büyüğe doğru sıralar
letters.reverse() # diziyi ters çevirir az önce küçükten büyüğe sıralamıştık artık büyükten küçüğe oldu
print(numbers) 
print(letters)

print(len(numbers))
print(len(letters)) # yine eleman sayısını gösterirler değişen bir şey yok

print(numbers.count(10)) # 10 değerinin kaç kere geçtiğini bize söyler
print(letters.count("a")) # a değerinin kaç kere geçtiğini bize söyler

numbers.clear() # dizinin bütün elemanlarını temizler şuanda numbers içi boş bir dizi
print(numbers)

# list methods in python yazarak hepsine ulaşabilirsin 