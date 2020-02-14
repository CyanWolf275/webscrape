#This file keeps clicking the show more button on a peing user's page until all the questions are shown. 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()
driver.get("https://peing.net/ja/nero0x0")#Complete this with the user's name
j = 0
for i in range(6, 7 + 500, 5):#The number 100 can be adjusted according to the number of the questions
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div[1]/div/div[6]/div/div/div/div[" + str(i) + "]/div")))
    driver.execute_script("arguments[0].click();", driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[6]/div/div/div/div[" + str(i) + "]/div"))
    print(j)
    j += 1
input()
driver.close()
