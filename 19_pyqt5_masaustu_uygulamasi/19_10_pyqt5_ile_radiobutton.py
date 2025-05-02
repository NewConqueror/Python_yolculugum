import sys
from PyQt5 import QtWidgets
from ders134_radiobuttonForm import Ui_MainWindow

class Form(QtWidgets.QMainWindow):

    def __init__(self):

        super(Form,self).__init__()

        self.arayüz = Ui_MainWindow()
        self.arayüz.setupUi(self)

        self.arayüz.radioButton.setChecked(True)   # default olarak seçili gelsin dedik
        self.arayüz.radioButton_5.setChecked(True)

        self.arayüz.radioButton.toggled.connect(self.tiklaulke)
        self.arayüz.radioButton_2.toggled.connect(self.tiklaulke)
        self.arayüz.radioButton_3.toggled.connect(self.tiklaulke)
        self.arayüz.radioButton_4.toggled.connect(self.tiklaulke)

        self.arayüz.radioButton_5.toggled.connect(self.tiklaegitim)
        self.arayüz.radioButton_6.toggled.connect(self.tiklaegitim)
        self.arayüz.radioButton_7.toggled.connect(self.tiklaegitim)
        self.arayüz.radioButton_8.toggled.connect(self.tiklaegitim)

        self.arayüz.pushButton.clicked.connect(self.secilenalulke)
        self.arayüz.pushButton_2.clicked.connect(self.secilenalegitim)

    
    def tiklaulke(self):
        rb = self.sender()

        if rb.isChecked():
            print("seçilen ulke: "+ rb.text())

    def secilenalulke(self):

        items = self.arayüz.groupBox.findChildren(QtWidgets.QRadioButton)

        for rb in items:
            if rb.isChecked():
                self.arayüz.label.setText("secilen ulke: "+ rb.text())


    def tiklaegitim(self):
        rb = self.sender()

        if rb.isChecked():
            print("seçilen eğitim: "+ rb.text())

    def secilenalegitim(self):

        items = self.arayüz.groupBox_2.findChildren(QtWidgets.QRadioButton)

        for rb in items:
            if rb.isChecked():
                self.arayüz.label_2.setText("secilen egitim: "+ rb.text())

    






def goster():

    uygulama = QtWidgets.QApplication(sys.argv)

    win = Form()

    win.show()

    sys.exit(uygulama.exec_())

goster()