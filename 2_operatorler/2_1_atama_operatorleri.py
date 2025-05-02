# x=5
# y=10
# z=20

x,y,z = 5,10,20  # böyle bir atama yolu var

x,y = y,x   # yer değiştirdiler python da böyle kolayca oluyor diğerlerinde temp değişkene ihtiyaç vardı x=10 y=5 şuan

x+=5    # x = x + 5
x-=5    # x = x - 5
x*=5    # x = x * 5 
x/=5    # x = x / 5
x%=5    # x = x % 5
x//=5   # x = x // 5
x**5    # x = x ** 5  üs almaydı


values = 1, 2, 3
values2 = 1, 2, 3, 4, 5
print(values)
print(type(values))  # tuple tipinde bir liste

x,y,z = values  # 3 e 3 olduğu için normal bir şekilde atar
#x,y,z = values2 # dersek hata verir çünkü 3 tane değişken var biz 5 tane sokmaya çalışıyoruz
                # aynı şey az için de geçerli 1,2 olsaydı bu sefer fazla değil az olduğu için hata alıcaktık

x,y,*z = values2 # bunda hata vermez x=1 y=2 olur ama z ye dizi şeklinde atar yani z = [3,4,5] olur
print(x,y,z)
print(z[2]) # mesela 5 değerini döndürür