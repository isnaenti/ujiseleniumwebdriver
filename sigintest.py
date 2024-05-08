from selenium import webdriver
# menggunakan fungsi By
from selenium.webdriver.common.by import By
# menggunakan fungsi time
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=options)

# Navigasi ke halaman yang mengandung elemen
driver.get("https://www.zennioptical.com/?gad_source=1&gclid=EAIaIQobChMIr4Pe3cH9hQMV0RiDAx1z-wuXEAAYASAAEgIfb_D_BwE&gclsrc=aw.ds#")

# Temukan elemen dengan XPath
create_account_link = driver.find_element_by_xpath("//a[@href='/login?tab=createaccount']")

# Lakukan tindakan pada elemen (contoh: klik tautan)
create_account_link.click()

driver.find_element_by_name("firstName").send_keys("Isnaenti")

driver.find_element_by_name("lastName").send_keys("Nur")

driver.find_element_by_name("email").send_keys("isnaenti16@gmail.com")

driver.find_element_by_name("password").send_keys("Kodokberjamur16")

time.sleep(5)

checkbox_element = driver.find_element_by_id("register_form_agreeTerms")

# Mencentang checkbox
checkbox_element.click()

create_account_button = driver.find_element(By.XPATH, "//button[@class='ant-btn ant-btn-primary ant-btn-block']//span[text()='CREATE ACCOUNT']")

# Klik tombol
create_account_button.click()

# Tutup WebDriver
driver.quit()
