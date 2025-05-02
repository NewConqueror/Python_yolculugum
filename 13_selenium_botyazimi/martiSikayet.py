
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import   By



import time

class Cimer:
    def __init__(self, tc, ad,soyad,dg,serino,cep):

        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)

        self.tc = tc
        self.ad = ad
        self.soyad = soyad
        self.dg = dg
        self.serino = serino
        self.cep = cep
    
    def sikayet(self):
        self.browser.get("https://www.cimer.gov.tr")
        time.sleep(2)
    
        tc = self.browser.find_element_by_xpath("//*[@id='Vatandas_TcKimlikNo']")
        ad = self.browser.find_element_by_xpath("//*[@id='Vatandas_Ad']")
        soyad = self.browser.find_element_by_xpath("//*[@id='Vatandas_Soyad']")
        dg = self.browser.find_element_by_xpath("//*[@id='Vatandas_DogumTarihi']")
        serino = self.browser.find_element_by_xpath("//*[@id='Vatandas_SeriSiraNo']")
        cep = self.browser.find_element_by_xpath("//*[@id='Vatandas_CepTelefonu']")

        
        tc.send_keys(self.tc)
        ad.send_keys(self.ad)
        soyad.send_keys(self.soyad)
        dg.send_keys(self.dg)
        serino.send_keys(self.serino)
        cep.send_keys(self.cep)

        btnSubmit = self.browser.find_element_by_xpath("//*[@id='Vatandas_KisiselVerilerinKorunmasiKanunu']")
        btnSubmit.click()

        btnTikla = self.browser.find_element_by_xpath("//*[@id='btnOnayKoduGonder']")
        btnTikla.click()
        time.sleep(2)

   



cimer = Cimer("13652464090","fatih","yeni","28.07.2004","11111111","5374201745")
# login
cimer.sikayet()



    

