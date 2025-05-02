def selamla(ad):
    print("merhaba ",ad)

print(selamla("fatih"))
print(selamla) # fonksiyonun bellek adresini döndürür

merhaba = selamla

print(merhaba)  # ikisinin de bellek adresi aynı olur
print(selamla)  

del merhaba

print(selamla) # selamla hala var olur merhabayı sildiğimiz için o da yok olmaz


# encapsulation kapsülleme
def dis(sayi): # 10
    print("dis")

    def içarttir(sayi):
        print("iç")
        return sayi + 1  # 10 + 1 = return 11
    
    sayi2 = içarttir(sayi) # sayi2 = içarttir(10)
    print(sayi,sayi2)  # 10, 11
    
    
dis(10)
# içarttır() dış olmadan çalışamaz dış olmadan bir anlamı yok
 


def faktoriyel(sayi):

    if not isinstance(sayi,int): # isinstance hazır fonksiyonu sayi int mı diye bakar
        raise TypeError("sayi integer olmalı")

    if not (sayi >=0):
        raise ValueError("sayi 0 veya pozitif olmalı")
    
    def içfaktoriyel(sayi): # içfaktoriyel(5)
        if(sayi<=1):
            return 1
        
        return sayi * içfaktoriyel(sayi-1) # 5 * içfaktoriyel(4) =  5 * 4 * içfaktoriyel(3)=return 5 * 4 * 3 * 2 *1

    return içfaktoriyel(sayi) # return 120

print(faktoriyel(5))

try:
    #print(faktoriyel("4"))
    print(faktoriyel(-2))
except Exception as ex:
    print(ex)