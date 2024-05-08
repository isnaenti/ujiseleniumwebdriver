# ujiseleniumwebdriver

Buatlah program pengujian untuk aplikasi website untuk proses registrasi akun pada suatu sistem. Buatlah langkah-langkah pengujian menggunakan selenium webdriver.

Tentu, berikut adalah contoh langkah-langkah pengujian menggunakan Selenium WebDriver untuk proses registrasi akun pada suatu sistem:

1. **Persiapan Lingkungan:**
   Pastikan Python telah terinstal di komputer Anda. Instalasi Selenium WebDriver juga diperlukan. Gunakan pip untuk menginstalnya:
   ```
   pip install selenium
   ```

2. **Import Library:**
   Impor modul selenium WebDriver dan modul time untuk mengatur waktu tunggu.
   ```python
   from selenium import webdriver
   from selenium.webdriver.common.by import By
   import time
   ```

3. **Inisialisasi WebDriver:**
   Inisialisasikan driver WebDriver yang sesuai dengan browser yang ingin Anda gunakan. Di sini, kita akan menggunakan Chrome WebDriver.
   ```python
   options = webdriver.ChromeOptions()
   options.add_experimental_option('detach', True)
   driver = webdriver.Chrome(options=options)
   ```

4. **Navigasi ke Halaman Registrasi:**
   Gunakan metode `get()` untuk membuka halaman registrasi.
   ```python
   driver.get("https://www.zennioptical.com/?gad_source=1&gclid=EAIaIQobChMIr4Pe3cH9hQMV0RiDAx1z-wuXEAAYASAAEgIfb_D_BwE&gclsrc=aw.ds#")
   ```

5. **Isi Formulir Registrasi:**
   Temukan elemen-elemen HTML yang diperlukan untuk mengisi formulir registrasi dan kirimkan data palsu.
   ```python
   create_account_link = driver.find_element(By.XPATH, "//a[@href='/login?tab=createaccount']")

   create_account_link.click()

   driver.find_element(By.NAME, "firstName").send_keys("Isnaenti")
   driver.find_element(By.NAME, "lastName").send_keys("Nur")
   driver.find_element(By.NAME, "email").send_keys("isnaenti16@gmail.com")
   driver.find_element(By.NAME, "password").send_keys("Kodokberjamur16")

   time.sleep(2)

   checkbox_element = driver.find_element(By.ID, "register_form_agreeTerms")
    if not checkbox_element.is_selected():
        checkbox_element.click()
   ```

6. **Kirim Formulir Registrasi:**
   Temukan tombol atau elemen yang mengirimkan formulir dan kirimkan formulir.
   ```python
   create_account_button = driver.find_element(By.XPATH, "//button[@class='ant-btn ant-btn-primary ant-btn-block']//span[text()='CREATE ACCOUNT']")
   create_account_button.click()

   time.sleep(5)
   ```

7. **Menutup WebDriver:**
   Setelah pengujian selesai, tutup WebDriver.
   ```python
   driver.quit()
   ```

9. **Menjalankan Program:**
   Panggil file pada terminal dengan mengetik.
   ```bash
   python sigintest.py
   ```