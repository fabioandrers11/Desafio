from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re

driver = webdriver.Chrome()

driver.get('https://www.pingodoce.pt/')

time.sleep(5)

button = driver.find_element(By.CLASS_NAME, "deny")
button.click()

time.sleep(2)

button1 = driver.find_element(By.ID, "onetrust-accept-btn-handler")
button1.click()

time.sleep(2)

SearchInput = driver.find_element(By.NAME, "s")
SearchInput.send_keys("Receitas de Panquecas")
SearchInput.submit_button.click()

matches = re.findall(r'panquecas')
count = len(matches)
print(f'A palavra "panquecas" aparece {count} vezes.')

driver.close()

