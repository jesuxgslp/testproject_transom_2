import time
import pytest
from selenium import webdriver

chromeDriver = webdriver.Chrome()
chromeDriver.get("http://localhost:8000/app/create_carro")
#chromeDriver = webdriver.Chrome(executable_path="C:\Users\Admin......\")
#get controls
nameControl = chromeDriver.find_element_by_name('name')
bussinesNameControl = chromeDriver.find_element_by_name('bussinesName')
rfcControl = chromeDriver.find_element_by_name('rfc')
addresControl = chromeDriver.find_element_by_name('addres')
phoneControl = chromeDriver.find_element_by_name('phone')
emailControl = chromeDriver.find_element_by_name('email')
createClientControl = chromeDriver.find_element_by_name('create')

#set values
nameControl.send_keys('Oxxo')
bussinesNameControl.send_keys('Tiendas Oxxo S.A. de C.V.') 
rfcControl.send_keys('OXXO1234TR0')
addresControl.send_keys('Av. Carranza #1230')
phoneControl.send_keys('123123123')
emailControl.send_keys('tiendas@oxxo.com.mx')
time.sleep(10)
#chromeDriver.implicitly_wait(10)

#chromeDriver.maximize_window()
createClientControl.click()