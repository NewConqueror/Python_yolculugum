from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

# Kullanıcı bilgileri
email_address = "youremail@gmail.com"
password = "yourpassword"
recipient_email = "recipientemail@gmail.com"
subject = "Test Subject"
message = "This is a test email sent using Selenium."

# Yeni Chrome profil dizini oluştur
chrome_profile_path = os.path.join(os.getcwd(), "chrome_profile")

# Eğer dizin yoksa oluştur
if not os.path.exists(chrome_profile_path):
    os.makedirs(chrome_profile_path)

# Chrome seçeneklerini ayarla
options = webdriver.ChromeOptions()
options.add_argument(f"user-data-dir={chrome_profile_path}")

# ChromeDriver'ı yükle ve başlat
service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://mail.google.com")

try:
    # Email giriş
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="identifierId"]'))
    )
    email_input.send_keys(email_address)
    email_input.send_keys(Keys.RETURN)

    # Şifre giriş
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@name="password"]'))
    )
    password_input.send_keys(password)
    password_input.send_keys(Keys.RETURN)

    # Gmail ana sayfasının yüklenmesini bekle
    compose_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@class="T-I T-I-KE L3"]'))
    )
    compose_button.click()

    # Alıcı email adresi
    to_input = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@name="to"]'))
    )
    to_input.send_keys(recipient_email)

    # Konu
    subject_input = driver.find_element(By.XPATH, '//*[@name="subjectbox"]')
    subject_input.send_keys(subject)

    # Mesaj
    message_body = driver.find_element(By.XPATH, '//*[@class="Am Al editable LW-avf tS-tW"]')
    message_body.send_keys(message)

    # Gönder butonuna tıkla
    send_button = driver.find_element(By.XPATH, '//*[@class="T-I J-J5-Ji aoO v7 T-I-atl L3"]')
    send_button.click()

    print("Email gönderildi!")

finally:
    # Tarayıcıyı kapat
    time.sleep(60)  # İsteğe bağlı: 5 saniye bekle ve tarayıcıyı kapat
    driver.quit()
