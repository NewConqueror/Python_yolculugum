import sys 
from PyQt5 import QtWidgets 
from PyQt5.QtWidgets import QApplication,QMainWindow,QToolTip
from PyQt5.QtGui import QIcon


class mywindow(QMainWindow):

    def __init__(self):
        super(mywindow,self).__init__()

        self.setWindowTitle("ilk uygulama")          
        self.setGeometry(200,200,500,500)            
        self.setWindowIcon(QIcon("doctor who.jpg"))  
        self.setToolTip("benim tooltip im")   

        self.initUI()

    def initUI(self):

        self.labelad = QtWidgets.QLabel(self) 
        self.labelad.setText("adınız: ")     
        self.labelad.move(50,30)             

        self.labelsoyad = QtWidgets.QLabel(self)
        self.labelsoyad.setText("soyadınız: ")
        self.labelsoyad.move(50,70)

        self.lblsonuc = QtWidgets.QLabel(self)
        self.lblsonuc.resize(300,50)
        self.lblsonuc.move(150,150)

        self.txtad= QtWidgets.QLineEdit(self)
        self.txtad.move(150, 30)
        self.txtad.resize(200,32)

        self.txtsoyad = QtWidgets.QLineEdit(self)
        self.txtsoyad.move(150, 70)
        self.txtsoyad.resize(200,32)

    
           
        self.buton = QtWidgets.QPushButton(self)  
        self.buton.setText('Kaydet')
        self.buton.move(150,110)
        self.buton.clicked.connect(self.tikla)   
        
    def tikla(self):
        self.lblsonuc.setText("ad: "+self.txtad.text() + " soyad: "+ self.txtsoyad.text())


def pencere():

    uygulama = QApplication(sys.argv)

    win = mywindow()

    win.labelad.setText("yarraa")  # win nesnesi üzerinden de ulaşabilirsin

    win.show()   

    sys.exit(uygulama.exec_()) 

pencere()


