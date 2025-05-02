import sys # uygulamayı komut satırından çalıştırıcaz bir argüman göndermek lazım onun için import ettik
from PyQt5 import QtWidgets 
from PyQt5.QtWidgets import QApplication,QMainWindow,QToolTip
from PyQt5.QtGui import QIcon

def pencere():

    uygulama = QApplication(sys.argv)

    win = QMainWindow()

    win.setWindowTitle("ilk uygulama")          # başlık verdik
    win.setGeometry(200,200,500,500)            # konumu soldan 200 sağdan 200 boyutu ise 500 e 500 olsun dedik
    win.setWindowIcon(QIcon("doctor who.jpg"))  # sol üste ikon ekledik
    win.setToolTip("benim tooltip im")          # tooltip ekledik üzerinde biraz bekleyince geliyor

    win.show()   # uygulamayı görmek için buna ihtiyacımız var

    sys.exit(uygulama.exec_()) # çarpı ya tıkladığında uygulamadan çık demiş olduk

pencere()