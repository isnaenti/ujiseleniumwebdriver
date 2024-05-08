from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)

try:
    # Navigasi ke halaman yang mengandung elemen
    driver.get("https://www.zennioptical.com/?gad_source=1&gclid=EAIaIQobChMIr4Pe3cH9hQMV0RiDAx1z-wuXEAAYASAAEgIfb_D_BwE&gclsrc=aw.ds#")

    # Temukan elemen dengan XPath untuk membuat akun
    create_account_link = driver.find_element(By.XPATH, "//a[@href='/login?tab=createaccount']")

    # Klik tautan untuk membuat akun
    create_account_link.click()

    # Isi formulir pendaftaran
    driver.find_element(By.NAME, "firstName").send_keys("Isnaenti")
    driver.find_element(By.NAME, "lastName").send_keys("Nur")
    driver.find_element(By.NAME, "email").send_keys("isnaenti16@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("Kodokberjamur16")

    time.sleep(5)  # Tunggu beberapa detik sebelum mencari checkbox

    # Mencentang checkbox persetujuan
    checkbox_element = driver.find_element(By.ID, "register_form_agreeTerms")
    if not checkbox_element.is_selected():
        checkbox_element.click()

    # Temukan tombol "CREATE ACCOUNT" dan klik
    create_account_button = driver.find_element(By.XPATH, "//button[@class='ant-btn ant-btn-primary ant-btn-block']//span[text()='CREATE ACCOUNT']")
    create_account_button.click()

    time.sleep(5)  # Tunggu beberapa detik untuk melihat hasilnya

finally:
    # Tutup WebDriver
    driver.quit()
