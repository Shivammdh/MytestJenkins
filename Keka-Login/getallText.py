import time

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_kekalogin():
    print('building session')
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    print("-----------Keka Login page-----------")
    driver.get("https://app.keka.com/Account/KekaLogin?returnUrl=%2F")

    vd=driver.find_element(By.CLASS_NAME,"form-control")
    driver.execute_script("arguments[0].value='msys';",vd)

    #send the email and password to these fields
    driver.find_element(By.ID,"email").send_keys("ssharma@msystechnologies.com")

    driver.find_element(By.ID,"password").send_keys('Msystech@1906')
    driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
    time.sleep(5)
    name=driver.find_element(By.CSS_SELECTOR,"span.profile-name").text
    print(f"Hi {name} You are successfully login on keka portal.")

    ## DO STUFF
    driver.quit()
