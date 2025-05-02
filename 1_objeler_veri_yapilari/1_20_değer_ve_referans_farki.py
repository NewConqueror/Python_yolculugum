# değer olarak 
x = 5
y = 25
x=y
y=10
print(x,y) # y de yaptığım değişiklik x i etkilemedi çünkü değer ikisi de

# referans olarak

a = ["elma","muz"]
b = ["elma","muz"]

a=b

b[0] = "hindistan cevizi"

print(a,b) # ikisi de hindistan cevizi , muz çıktısını verdi çünkü listeler birer pointer
# değerlerini değil adreslerini eşitledik 
