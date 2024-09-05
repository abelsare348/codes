from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import getpass
from bs4 import BeautifulSoup


login_id=input("Enter your email id which you registered for LinkedIN\n")
password=getpass.getpass('Please enter the password\n')

driver = webdriver.Chrome()
driver.get("https://www.linkedin.com/uas/login")

time.sleep(5)

username=driver.find_element(By.ID,'username')
passwd=driver.find_element(By.ID,'password')

username.send_keys(login_id)
passwd.send_keys(password) 

driver.find_element(By.XPATH, "//button[@type='submit']").click()

driver.get('https://www.linkedin.com/in/aniket-belsare-56557a217')

soup = BeautifulSoup(driver.page_source, 'html.parser')

content=soup.find('div',class_='mt2 relative')

name=content.find('div',class_="MjkoDHLbisFtJAAWEaxICABuwiWWxAwMv")

title_name=name.find('div',class_='text-heading-xlarge inline t-24 v-align-middle break-words')
print(title_name)
time.sleep(10)

