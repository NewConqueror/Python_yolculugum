# Question
class Soru:
    # constructor metot
    def __init__(self,soru,seçenekler,cevap):
        self.soru = soru
        self.seçenekler = seçenekler
        self.cevap = cevap
    # cevapları kontrol etmeye yarayan metot
    def cevapKontrol(self, cevap):
        return self.cevap == cevap # True ya da False değer döndürecek

# Quiz
class Quiz:
    # Quiz constructor ı
    def __init__(self, sorular):
        self.sorular = sorular
        self.puan = 0
        self.soruindex = 0
    # soruyu nesneye yükleyen metot
    def sorugetir(self):
        return self.sorular[self.soruindex]
    
    # soruyu ekrana getiren metot
    
    # burada soru.soru diyoruz çünkü gelen nesneler bir soru nesnesi
    # soru nesnesi oldukları için soru seçenekler cevap özelliklerine sahipler
    def soruyazdir(self):
        soru = self.sorugetir()
        print(f'Soru {self.soruindex + 1}: {soru.soru}') # olm şurda soru gelmediği için kafayı yedim amk ya
#                                                          meğer öyleymiş harbiden ama çok garip haci
        for q in soru.seçenekler:
            print('-'+ q)
        
        cevap = input('cevap: ')
        self.tahmin(cevap)
        self.soruyükle()

    def tahmin(self, answer):
        question = self.sorugetir()
        # gelen değişkenler soru nesnesi oldukları için cevapkontrol fonksiyonuna sahipler
        if question.cevapKontrol(answer):
            self.puan += 1
        self.soruindex += 1

    def soruyükle(self):
        if len(self.sorular) == self.soruindex:
            self.puangöster()
        else:         
            self.sürecigöster()  
            self.soruyazdir()

    def puangöster(self):
        print('puan: ', self.puan)

    def sürecigöster(self):
        toplamsoru = len(self.sorular)
        soruno = self.soruindex + 1

        if soruno > toplamsoru:
            print('Quiz bitti.')
        else:
            print(f'Question {soruno} of {toplamsoru}'.center(100,'*'))

q1 = Soru('en iyi programlama dili hangisidir ?', ['C#','python','javascript','java'], 'python')
q2 = Soru('en popüler programlama dili hangisidir ?', ['python','javascript','C#','java'], 'python')
q3 = Soru('en çok kazandıran programlama dili hangisidir ?', ['C#','javascript','java','python'], 'python')
q4 = Soru('en çok sevilen programlama dili hangisidir ?', ['C#','javascript','java','python'], 'python')
q5 = Soru('en kolay programlama dili hangisidir ?', ['C#','javascript','java','python'], 'python')


soruliste = [q1,q2,q3,q4,q5]

quiz = Quiz(soruliste)

quiz.soruyükle()