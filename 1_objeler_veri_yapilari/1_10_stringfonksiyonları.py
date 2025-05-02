mesaj = " MerHaba. benim Adim. fAtih yeNi"

mesaj=mesaj.upper() # hepsini büyük yazar
mesaj=mesaj.lower() # hepsini küçük yazar
mesaj=mesaj.title() # hepsinin baş harfini büyük yazar
mesaj=mesaj.capitalize() # sadece ilk harfi büyük yazar kalanı küçük boşluk varsa başta boşluğu büyük yapmış gibi olur
mesaj=mesaj.strip() # cümlenin başında boşluk varsa boşluğu siler kalanı küçük

mesaj=mesaj.split() # boşluğa göre ayırıp bir dizi içine atar her bir kelime bir dizi elemanı olur

#mesaj=mesaj.split(".") # noktaya göre ayırıp dizi içine atar
# print(mesaj)
# print(mesaj[1])

#mesaj = "---".join(mesaj) # neye göre ayırdıysak o kısmı verdiğimiz şey ile doldurur * deseydik * ile dolduracaktı

#index = mesaj.find('benim') # eğer kelime varsa ilk harfin index numarasını döndürecek eğer kelime yoksa -1 döndürücek
#print(index)

# varmi = mesaj.startswith('M') # M ile başlıyorsa True yoksa False döndürecek
# varmi = mesaj.endswtih('i') # i ile bitiyorsa True yoksa False 

#mesaj = mesaj.replace(' ', '*') # şunu şu ile değiştir ilk girdiğini bulur onun yerine 2.yi yazar yani boşlukları bulacak ve yerine * yazacak
#mesaj = mesaj.replace('ö','u').replace('ü','u') türkçe karakterleri değiştirebiliriz vs vs

#mesaj = mesaj.center(50,'*') # cümle için 50 kelimelik bir yer ayırır ve tam ortasına bizim cümleyi yazar boşta kalan kısımları da * ile doldurur
# örneğin strr = "merhabaa"  str=str.center(14,'*') yazarsak ***merhabaa*** yazar
print(mesaj)
# google a string methods python yaz hepsi çıkar