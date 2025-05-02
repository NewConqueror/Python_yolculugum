name = "fatih yeni"

for letter in name:
    if(letter == "a"):
        break
    print(letter)

for letter in name:
    if(letter == "a"): # böyleyken sıkıntı yok direkt atlar ama while da sıkıntı
        continue
    print(letter)

x=0
# while x < 5:
#     if(x==2):
#         break
# print(x)
# x+=1

while x < 5:
    x+=1  # continue da direkt koşula döner sonda arttırırsak x hiç değişmediği için hep if e girer ve continue yapıp
          # başa  döner onun için python da continue kullandığın zaman arttırma ifadesini başa yazman gerekiyor
    if(x==2):
        continue
print(x)

 # 1 den 100 e kadar tek sayılar toplamı
x=0
toplam =0
while x <=100:
    x+=1
    if(x %2 ==0):
        continue
    else:
        toplam+=x



