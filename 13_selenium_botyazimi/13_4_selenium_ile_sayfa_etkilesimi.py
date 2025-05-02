from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

url = "http://github.com"

driver.get(url)


searchInput = driver.find_element("/html/body/div[1]/div[1]/header/div/div[2]/div/div/qbsearch-input/div[1]/div/modal-dialog/div/div/div/form/query-builder/div[1]/div[1]/div/div[2]/input")
time.sleep(1)
driver.maximize_window()
time.sleep(3)
searchInput.send_keys("python")
time.sleep(2)

searchInput.send_keys(Keys.ENTER)
# time.sleep(2)

# sonuc = driver.page_source
# print(sonuc) # kaynak kodlarını alıp onun üzerinden işlem yapabiliriz alternatif olarak

sonuc = driver.find_elements_by_css_selector(".repo-list-item h3 a")


for element in sonuc:
    print(element.text)