from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

s = Service(executable_path='')
driver = webdriver.Chrome(service=s)
wait = WebDriverWait(driver, 20)
driver.get("https://www.smartprix.com/mobiles")

def click_element(xpath):
    element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
    time.sleep(0.5)
    driver.execute_script("arguments[0].click();", element)

click_element("//*[@id='app']/main/aside/div/div[5]/div[2]/label[1]/span")
time.sleep(1)
click_element("//*[@id='app']/main/aside/div/div[5]/div[2]/label[2]/span")
time.sleep(1)

old_height = driver.execute_script("return document.body.scrollHeight")
while True:
    try:
        load_more = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='app']/main/div[1]/div[2]/div/div[3]")))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", load_more)
        time.sleep(0.5)
        driver.execute_script("arguments[0].click();", load_more)
    except Exception:
        break

    time.sleep(2)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == old_height:
        break
    old_height = new_height

html = driver.page_source
with open("smartprix.html", "w", encoding="utf-8") as f:
    f.write(html)

driver.quit()
