from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time 

driver = webdriver.Chrome()
query="laptop"
driver.get(f"https://www.amazon.in/s?k={query}&crid=82JPIJIXTHA6&sprefix=laptop%2Caps%2C230&ref=nb_sb_noss_1")
elem = driver.find_element(By.CLASS_NAME, "aok-relative")
time.sleep(2)
print(elem.get_attribute("outerHTML"))

driver.close()