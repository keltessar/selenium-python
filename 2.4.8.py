from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import math
import time


try:

    link = 'http://suninjuly.github.io/explicit_wait2.html'
    browser = webdriver.Chrome()
    browser.get(link)    

    WebDriverWait(browser, 14).until(EC.text_to_be_present_in_element((By.ID, 'price'), '100'))
    button = browser.find_element_by_tag_name("button")
    button.click()

    x = int(browser.find_element_by_id('input_value').text)
    result = math.log(abs(12*math.sin(x)))

    input_res = browser.find_element_by_id('answer')
    input_res.send_keys(str(result))
   
    button2 = browser.find_element_by_id("solve")
    button2.click()
    

finally:

    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

#empty string in the end