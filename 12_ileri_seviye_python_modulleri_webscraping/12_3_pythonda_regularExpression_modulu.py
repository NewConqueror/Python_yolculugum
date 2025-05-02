import re  # regular expression  re modülü kullanımı

sonuc = dir(re) # bir sürü var biz findall search split ve match e bakıcaz

string = "python kursu: python programlama rehberiniz | 40 saat"

sonuc = re.findall("python",str) # string veya regex ile oluşturulmuş bir ifade ve nerede arayacağını söylüyoruz

sonuc = len(sonuc)  # findall metodu bize bir liste döndürüyor kaç elemanlı old bulmak için len kullandık

sonuc = re.split(" ",string) # boşluğa göre böl deriz bu da bir dizi döndürür

sonuc = re.split("r",string) # r harfine göre böl deriz

sonuc = re.sub(" ","-",string)  # substringten geliyor " " karakterini - karakteri ile değiştirir verdiğimiz stringte
sonuc = re.sub("\s","-",string) # aynı şeyi diyorlar \s  boşluk karakteri anlamına gelir

sonuc = re.search("python",string)#bize bir tane match objesi döndürür span =(0,6) gibi özellikleri var ilk bulduğunu gösterir

sonuc = sonuc.span() # sonuc artık bir match objesi oldu  (0,6) döndürür
sonuc = sonuc.start() # 0 döndürür 0.karakterden başladığı için
sonuc = sonuc.end()  #6 döndürür 6.karakterde bittiği için
sonuc = sonuc.group() # bulduğu ifadeyi gösterir
sonuc = sonuc.string  # nerde aradığını yani hangi stringte aradığını gösterir

print(sonuc)



# regular expressions


"""
    [] - Köşeli parantezler arasına yazılan bütün karakterler
         aranır.
         [abc] => a      : 1 match
                  ac     : 2 match 
                  Python : No matches
         [a-e]  => [abcde]
         [1-5]  => [12345]
         [0-39] => [01239]   
         [^abc] => abc dışındaki karakterler.
         [^0-9] => rakam olmayan karakterler.
"""

sonuc = re.findall("[abc]",string) # abc karakterlerini bulur ve liste içine atar
sonuc = re.findall("[sat]",string) # sat karakterlerini bulur ve liste içine atar
sonuc = re.findall("[a-e]",string) # a dan e ye kadar olan karakterleri bulur ve liste içine atar re.findall("[abcde]") ile aynı
sonuc = re.findall("[a-z]",string) # a dan z ye kadar olanlar vs
sonuc = re.findall("[0-5]",string) # 0 dan 5 e kadar olanları bulur re.findall("[012345]") ile aynı
sonuc = re.findall("[^abc]",string) # abc dışında kalan her karakteri liste içine atar
sonuc = re.findall("[^0-9]",string) # rakam olmayanlar dışında kalanları listeler
sonuc = re.findall("[0-478]",string) # 0 dan 4 e kadar ve 7 8 e bakar [0123478] bunla aynı
 

"""
    . - Her hangi bir tek karakteri belirtir.
        .. => a    : No match
              ab   : 1 match
              abc  : 1 match
              abcd : 2 matches
    
"""

sonuc = re.findall("...",string) # bütün string i 3 lü gruplar halinde bize böler
sonuc = re.findall("py..on",string) #py on sabit ama ortası değişken python pyabon pycdon olsaydı bunları da yazıcaktı



"""
    ^ - Belirtilen string karakterlerle başlıyor mu ?
    ^a => a:    1 match
          abc:  1 match
          bac:  No match
"""

sonuc = re.findall("^p",string) # p ile başladığı için bize ['p'] yi gösterir
sonuc = re.findall("^k",string) # bütün stringin başı olmalı ama kursunda k başta olmaz kardeşim [] görürsün

"""
    $ - Belirtilen karakterle bitiyor mu ?
    a$ => a      : 1 match
          lamba  : 1 match
          Python : No match 
"""

sonuc = re.findall("t$",string) # t ile bittiği için  t yi döndürür ['t'] 40 saat 
sonuc = re.findall("saat$",string) # saat kelimesi ile bittiği için saat i döndürür ['saat']
sonuc = re.findall("saatt$",string) # saatt ile bitmediği için hata [] döndürür


"""
     * - Bir karakterin sıfır ya da daha fazla sayıda olmasını 
         kontrol eder.
         ma*n => mn     : 1 match
                 man    : 1 match
                 maaan  : 1 match
                 main   : No match (a' nın arkasına n gelmiyor.) 
"""

sonuc = re.findall("sa*t")  # st sat da saat da saaaat da olsa yazar ama salt olsa olmaz çünkü araya l giriyor




"""
     + - Bir karakterin bir ya da daha fazla sayıda olmasını 
         kontrol eder.
         ma+n => mn     : No match
                 man    : 1 match
                 maaan  : 1 match
                 main   : No match (a' nın arkasına n gelmiyor.) 
"""

sonuc = re.findall("sa+t") # aynı yıldız gibi tek farkı 0 da yani st yi göstermez


"""
    ? - Bir karakterin sıfır ya da bir kez olmasını 
        kontrol eder.
        ma+n => mn     : No match
                man    : 1 match
                maaan  : 1 match
                main   : No match (a' nın arkasına n gelmiyor.) 
"""

sonuc = re.findall("sa?t") # st sat döndürür saat te 2 kez a old için olmaz 


"""
    {} - Karakter sayısını kontrol eder.
        al{2}   => a karakterinin arkasına l karakteri 2 kez tekrarlamalı.
        al{2,3} => a karakterinin arkasına l karakteri en az 2 en fazla 3 kez tekrarlamalı.
        [0-9]{2,4} => en az 2 en çok 4 basamaklı sayılar.
"""

sonuc = re.findall("a{2}") # a karakteri aa şeklinde olmalı
sonuc = re.findall("[0-9]{2}") # 2 basamaklı sayıları gösterir


"""
    | - alternatif seçeneklerden birinin gerçekleşmesi gerekir.
        a|b => a ya da b
            cde =>    no match
            ade =>    1 match
            acdbea => 3 match 
"""


"""
    () - gruplamak için kullanılır.
         (a|b|c)xz => a,b,c karakterlerinin arkasına xz gelmelidir. axz bxz cxz hepsi benim için geçerli
""" 


sonuc = re.findall("\Apython",string)
sonuc = re.findall("saat\Z",string)

"""
    \ - Özel karakterleri aramamızı sağlar.
        \$a => $ karakterinin arkasına a karakterinin arar. Yani
               $ regular exp. engine tarafından yorumlanmaz.
    \A - Belirtilen karakter string in başında mı ?
         \Athe => the string in başındamı
        result = re.findall("\APython", str)
        result = re.findall("saat\Z", str)
    \Z - Belirtilen karakter string in sonunda mı ?
         the\Z => the string in sonunda mı
    \b - Belirtilen karakter kelimenin in başında ya da sonunda mı ?
         \bthe => the kelimenin in başında mı?
         the\b => the kelimenin in sonunda mı?
    \B - Belirtilen karakter kelimenin in başında ya da sonunda değil mı ?
         \Bthe => the kelimenin in başında değil mi?
         the\B => the kelimenin in sonunda değil mi?
    
    \d - [0-9] ile aynı anlama gelir yani rakamları arar.
         \d => 12abc34
    \D - [^0-9] ile aynı anlama gelir yani rakam olmayanları arar.
         \D => 1ab44_50
    \s - Boşluk karakterlerini arar.  
    \S - Boşluk karakterleri dışındakiler.
    \w - Alfabetik karakterler, rakamlar ve alt çizgi karakteri.
    \W - \w nin tam tersi
    
"""

# kalanları da google python regular expression yazarak bul 