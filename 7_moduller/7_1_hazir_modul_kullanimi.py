# YÖNTEM 1

import math   #kütüphaneyi bu şekilde dahil ediyoruz

value = dir(math)  # kütüphanede kullanılabilecek bütün fonksiyonları gösterir
print(value) 

value = help(math) # bütün fonksiyonların nasıl kullanılacağını açıklar gösterir
print(value)

value = help(math.factorial) # sadece factorial fonksiyonunun kullanımını gösterir

value = math.sqrt(49)
value = math.factorial(5)
value = math.floor(5.6)
value = math.ceil(5.6)


import math as islem  # math kütüphanesine islem takma adını verdik yani islem ile çağırabiliriz

value = islem.factorial(5)


# YÖNTEM 2

from math import * # mat kütüphanesinden her şeyi dahil et her şey kullanıma açık

def sqrt(x):
    print("x : ",x)

from math import factorial,sqrt  # sadece factorial ve sqrt fonksiyonları kullanıma açık diğerlerini kullanamazsın

def sqrt(x):
    print("x: ",x) # eğer böyle yaparsak yani math ın sqrt sinden sonra tanımlarsak bizim sqrt geçerli olur
#                   yani sqrt(9) dersek  x: 9 görürüz


value = factorial(5)
value = sqrt(9)

value = ceil(9.8) # ceil i yukarıda dahil etmediğimiz için çağıramayız hata verir

value = sqrt(9) # en son tanımlanan sqrt geçerli olur math ın sqrt daha altta olduğu için o geçerli oldu
#                  sqrt(9) dersek   3.0 görürürüz

