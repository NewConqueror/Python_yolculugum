import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QPalette, QColor              # renk eklemek için Grafiksel arayüz ü ve palet, renk sınıfını yükledik

class renksinif(QWidget):

    def __init__(self, renk):
        super(renksinif, self).__init__()

        self.setAutoFillBackground(True)     # arka planı full doldurmak için True yapmamız lazım

        palet = self.palette()            # palet oluşturmamız gerekiyor C# taki gibi kalem gibi 
        palet.setColor(QPalette.Window, QColor(renk)) # setcolor ile palet objesi alıcağını ve rengi veriyoruz
        self.setPalette(palet)                        # paleti böyle kullanıyoruz


class AnaForm(QMainWindow):

    def __init__(self):
        
        super(AnaForm, self).__init__()
        self.setGeometry(200,200,500,500)

        #layout = QtWidgets.QVBoxLayout() #  vertical yani dikey sıralanır alt alta ama kendi şekilleri yatay burda 
        #layout = QtWidgets.QHBoxLayout() # horizonal yani yatay sıralanır yan yana ama kendi şekilleri dikey burda 
        
        # layout.addWidget(renksinif("red"))
        # layout.addWidget(renksinif("blue"))
        # layout.addWidget(renksinif("green"))
        
        
        hlayout1 = QtWidgets.QHBoxLayout()
        hlayout1.addWidget(renksinif('red'))  # yatay sıralı 3 tane widget ekledik kırmızı mavi yeşil
        hlayout1.addWidget(renksinif('blue'))
        hlayout1.addWidget(renksinif('green'))
        hlayout1.setContentsMargins(30,20,30,30) # soldan 30 boşluk üstten 20 sağdan 30 satırlar arası 30
        hlayout1.setSpacing(50)                  # widgetlar arası boşluk 50

        hlayout2 = QtWidgets.QHBoxLayout()     # yatay sıralı 2 tane widget ekledik sarı siyah
        hlayout2.addWidget(renksinif('yellow'))
        hlayout2.addWidget(renksinif('black'))


        vlayout = QtWidgets.QVBoxLayout()
        vlayout.addLayout(hlayout1)        # dikey sıralı hlayout1 i ekledik yani ilk satırda kırmızı mavi yeşil,
        vlayout.addLayout(hlayout2)        # dikey sıralı hlayout2 i ekledik yani ikinci satırda sarı siyah olucak
               

        # glayout = QtWidgets.QGridLayout()         # form üzerinde matris oluşturuyoruz bildiğin başka fark yok

        # glayout.addWidget(renksinif('red'),0,0)    # 0 0 yani ilk satır ilk sütuna kırmızı
        # glayout.addWidget(renksinif('blue'),1,0)   # 1 0 yani ikinci satır ilk sütuna mavi
        # glayout.addWidget(renksinif('green'),0,1)  # 0 2 yani ilk satır ikinci sütuna yesil
        # glayout.addWidget(renksinif('yellow'),2,2) # 3 2 yani ucuncu satır ucuncu sütuna sarı   
        
        # widget = QWidget()
        # widget.setLayout(glayout)

        widget = QWidget()
        widget.setLayout(vlayout)

        # widget = QWidget()              # bir widget eklicez 
        # widget.setLayout(layout)    # o widget ı da eklemeden layout ile ilişkilendiriyoruz


        #widget = renksinif("blue")

        self.setCentralWidget(widget)   # ortaya yerleştirmek için bunu koyduk


def calistir():

    uygulama = QApplication(sys.argv)

    pencere = AnaForm()

    pencere.show()

    sys.exit(uygulama.exec_())


calistir()