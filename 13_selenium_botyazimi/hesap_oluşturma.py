from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

# Kullanıcı bilgileri
first_name = "YourFirstName"
last_name = "YourLastName"
username = "youruniqueusername123"
password = "yourpassword"
confirm_password = "yourpassword"

# ChromeDriver'ı yükle ve başlat
service = ChromeService(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://accounts.google.com/signup")

try:
    # Ad ve Soyad giriş
    first_name_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "firstName"))
    )
    first_name_input.send_keys(first_name)

    last_name_input = driver.find_element(By.ID, "lastName")
    last_name_input.send_keys(last_name)

    # Kullanıcı adı giriş
    username_input = driver.find_element(By.ID, "username")
    username_input.send_keys(username)

    # Şifre ve şifre onayı giriş
    password_input = driver.find_element(By.NAME, "Passwd")
    password_input.send_keys(password)

    confirm_password_input = driver.find_element(By.NAME, "ConfirmPasswd")
    confirm_password_input.send_keys(confirm_password)

    # İleri butonuna tıkla
    next_button = driver.find_element(By.XPATH, '//*[@id="accountDetailsNext"]/div/button')
    next_button.click()

    # CAPTCHA ve diğer güvenlik kontrolleri burada durabilir

    print("Hesap oluşturma girişimi tamamlandı.")

except Exception as e:
    print(f"Bir hata oluştu: {e}")

finally:
    # Tarayıcıyı kapat
    time.sleep(10)  # İşlemleri görmeniz için 10 saniye bekler
    driver.quit()
