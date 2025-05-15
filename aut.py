from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://tlconnect.teamlease.com/SecureLogin"
number="2309827"
password="Pcj@12345"



chrome_options = Options()
chrome_options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--ignore-ssl-errors")
driver = webdriver.Chrome(options=chrome_options)


driver.maximize_window()
driver.get(url)



try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "btnsubmit"))
    )
    print("Page has loaded, element is present.")
except:
    print("Timed out waiting for page to load.")
driver.find_element("id","txtuserid").send_keys(number)

driver.find_element("id","txtpassword").send_keys(password)

driver.find_element("id","btnsubmit").click()



try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "btnchkin"))
    )
    print("Page has loaded, element is present.")
except:
    print("Timed out waiting for page to load.")


driver.find_element("id","btnchkin").click()
    

# driver.find_element("id","btnchkin").send_keys(Keys.ENTER)




print("Successfully checked in for today.")

driver.close()

