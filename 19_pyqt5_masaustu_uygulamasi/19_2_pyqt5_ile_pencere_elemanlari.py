import sys 
from PyQt5 import QtWidgets 
from PyQt5.QtWidgets import QApplication,QMainWindow,QToolTip
from PyQt5.QtGui import QIcon

def pencere():

    uygulama = QApplication(sys.argv)

    win = QMainWindow()

    win.setWindowTitle("ilk uygulama")          
    win.setGeometry(200,200,500,500)            
    win.setWindowIcon(QIcon("doctor who.jpg"))  
    win.setToolTip("benim tooltip im")          

    labelad = QtWidgets.QLabel(win) # pencere nin içine ekleyeceğini söylüyoruz
    labelad.setText("adınız: ")     # settext ile ne yazacağını söylüyoruz
    labelad.move(50,30)             # move ile nerede olacağını söylüyoruz

    labelsoyad = QtWidgets.QLabel(win)
    labelsoyad.setText("soyadınız: ")
    labelsoyad.move(50,70)


    txtad= QtWidgets.QLineEdit(win) # Textbox ekledik QlineEdit kullanıyorsun
    txtad.move(150, 30)

    txtsoyad = QtWidgets.QLineEdit(win)
    txtsoyad.move(150, 70)

    def tıkla(self):
        print('butona tıklandı ad: '+ txtad.text()+ ' soyad: '+ txtsoyad.text())

    buton = QtWidgets.QPushButton(win)   # buton ekledik QPushButton ile 
    buton.setText('Kaydet')
    buton.move(150,110)
    buton.clicked.connect(tıkla)         # butona tıklandığında nereye bağlansın neyi çağırsın onu söyledik


    win.show()   

    sys.exit(uygulama.exec_()) 

pencere()









# QLabel
# QComboBox
# QCheckBox
# QRadioButton
# QPushButton
# QTableWidget
# QLineEdit
# QSlider
# QProgressBar