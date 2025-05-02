# error handling => hata yönetimi

try:
    x = int(input("x: "))
    y = int(input("y: "))
    print(x/y)
except ZeroDivisionError:       # 0 a bölünemediği için zero divison hatası için except yazdık
    print("sayi 0 a bölünemez ")
except ValueError:              # sayısal değer girilmediği zaman için valueeror hatası için except yazdık
    print("x ve y sayisal deger olmali") 
    print(ValueError)

try:
    x = int(input("x: "))
    y = int(input("y: "))
    print(x/y)
except (ZeroDivisionError,ValueError) as e: # ayrı ayrı amele gibi yazmaktansa tek bir except içinde birleştirdik
    print("yanlis bilgi girdiniz. ")        # ve e değişkenine o hata kodları gibi davranmasını söyleyip
    print(e)                                # hata sebepini kodlarını her neyse onu yazdırdık

try:
    x = int(input("x: "))
    y = int(input("y: "))
    print(x/y)
except:  #illa hata sebeplerini yazmak mı lazım genel bir except tanımladım her hata için o çalışsın zero value vs
    print("yanlis bilgi girdiniz") 
else:                       # hata mesajı almazsak da her şey yolunda yazsın
    print("her şey yolunda")

while True:
    try:
        x = int(input("x: "))
        y = int(input("y: "))
        print(x/y)
    except Exception as ex :           # sonuçta zero value vs hataları hepsi Exception sınıfının altında
        print("yanlis bilgi girdiniz") # e onu eklerim hata her neyse o bana söyler mis gibi
        print("hata: ",ex)
    else:                              # bir sıkıntı olmazsa döngüden çık
        break
    finally:                           # her şartta sıkıntı çıksın, düzgün çalışsın vs bu kod bloğu çalışır
        print("try except sonlandi")   # ve try except sonlandi mesajini bize gösterir