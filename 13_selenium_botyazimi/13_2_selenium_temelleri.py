from selenium import webdriver
import time

driver = webdriver.Chrome()

url = "http://github.com"

driver.get(url)

time.sleep(3)
print(driver.title)   # başlığı yazdırdık
driver.maximize_window() # başlangıçta küçük açılan pencereyi tam ekran yaptık
driver.save_screenshot("github.com-homepage.png")  # ekran görüntüsü aldık

url = "http://github.com/sadikturan"

driver.get(url)
print(driver.title)

if "sadikturan" in driver.title:              #başlıkta sadkikturan var mı oysa ekran görüntüsü al
    driver.save_screenshot("github-sadikturan.png")

time.sleep(3)

driver.back()      # geriye git
time.sleep(3)
driver.forward()   # ileriye git
time.sleep(3)

driver.close()    # kapat