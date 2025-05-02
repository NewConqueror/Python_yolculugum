# selenium bir web otomasyon kütüphanesidir
# selenium ile bir web sitesini ziyaret edip etkileşimde bulunabiliriz

from selenium import webdriver

driver = webdriver.Chrome()   # siteye uğramak için neyle açacağımızı söylememiz lazım chrom firefox vs

url = "http://sadikturan.com"  # url adresini almamız gerekiyor
 
driver.get(url) # get ile de url adresindeki yere gidiyoruz



