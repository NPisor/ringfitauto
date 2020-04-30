import time
from selenium import webdriver
from settings import email, password

#Navigate to Ring Fit Adventure amazon page
driver = webdriver.Chrome("C:\\Users\chromedriver.exe")
driver.get('https://www.amazon.com/Ring-Fit-Adventure-Nintendo-Switch/dp/B07XV4NHHN/ref=sr_1_2?dchild=1&keywords=ring+fit+adventure&qid=1587482744&sr=8-2');
time.sleep(1)
driver.find_element_by_id("buybox-see-all-buying-choices-announce").click()  #click first item
time.sleep(1)

#Locate buying buttons and cart buttons and selecting
driver.find_element_by_xpath("/html/body/div[2]/div[4]/div/div[1]/div[1]/div/div/div[2]/div[5]/div/form/span/span/span/input").click()   #click radio button one time purchase
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[7]/div[5]/div[1]/div[2]/div/div/div/form/div[2]/div[1]/div[1]/div/div[2]/div/div/div[3]/span/span/span/input").click()  #click buy now
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[2]/div[1]/div/div/div[4]/div/div/div/span[2]/span/a").click()
time.sleep(1)

#Login credentials for purchase
email_box = driver.find_element_by_name('email')
email_box.send_keys(email)
email_box.submit()
time.sleep(1)
password_box = driver.find_element_by_name('password')
password_box.send_keys(password)
password_box.submit()
time.sleep(1)

#Click purchase button
driver.find_element_by_xpath("/html/body/div[8]/div/div/div[2]/div/div[1]/div/div[1]/div[1]/div/span/span/input").click()
time.sleep(20)
driver.quit()