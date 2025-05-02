import sys
from PyQt5 import QtWidgets
from ders136_MessageBoxForm import Ui_MainWindow
from PyQt5.QtWidgets import QMessageBox   # MessageBox çıkması için bunu eklemeliyiz

class uygulama(QtWidgets.QMainWindow):

    def __init__(self):
        
        super(uygulama, self).__init__()


        self.arayüz = Ui_MainWindow()
        self.arayüz.setupUi(self)

        self.arayüz.pushButton.clicked.connect(self.showdialog)

    
    def showdialog(self):


        sonuc = QMessageBox.question(self, "uygulamayı kapa", "emin misin?",QMessageBox.Ok | QMessageBox.Cancel | QMessageBox.Ignore, QMessageBox.Cancel)
#   direkt bu şekilde hepsi bir arada da yapabiliriz başlık, ne yazsın, butonlar, default seçili buton
        if sonuc == QMessageBox.Ok:         # text ile uğraşmadan bu şekilde de yapabilirsin
            print("tıklandı")
            QtWidgets.qApp.quit()           # uygulamadan çıkmak için kullanılır
        else:
            print("tıklanmadı")



    #     msg = QMessageBox()                    # bir MessageBox nesnesi oluşturduk

    #     msg.setWindowTitle("uygulamayı kapa")  # MessageBox un Başlığını verdik
    #     msg.setText("emin misin?")             # MessageBox ın tam ortasında ne yazsın onu söyledik
    #     msg.setIcon(QMessageBox.Question)     # MessageBox ta ne ikonu olsun soru işareti uyarı vs intten bak
    #     msg.setIcon(QMessageBox.Warning) 

    #     msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel | QMessageBox.Ignore)
    #     hangi butonlar olsun onu söyledik OK butonu Cancel butonu Ignore butonu vs

    #     msg.setDefaultButton(QMessageBox.Ok)    # hangisi defult olarak seçili gelsin onu seçtik ok butonu 
    #     msg.setDetailedText("detaylar...")      # details kısmı açıyor kendisi onun altında ne yazsın onu dedik

    #     msg.buttonClicked.connect(self.popupButton)

    #     x = msg.exec_()    # butona tıklayınca bir geri dönüş alıcaz o geri dönüş x msg.exec_() ile alıyoruz
    #     print(x) # bir sayısal değer döndürür 1024 54526 vs vs gibi

    
    # def popupButton(self, i):

    #     print(i.text())      # tıkladığımız butonun text ini yazar

    #     if i.text() == "Ok":
    #         print("OKEYMİŞ AGA")
    #         QtWidgets.qApp.quit()
    #     elif i.text() == "Cancel":
    #         print("CANCELMIŞ AGA")
    #     else :
    #         print("IGNOREMUŞ AGA")



def göster():

    app = QtWidgets.QApplication(sys.argv)

    win = uygulama()

    win.show()

    sys.exit(app.exec_())

göster()