from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")


cookie = driver.find_element(By.ID, value = "cookie")


store = driver.find_elements(By.CSS_SELECTOR, value = "#store div")
upgrade_id = [i.get_attribute("id") for i in store]
timeout = time.time() + 5

while True:

    cookie.click()
    if time.time() > timeout:

        #get the cookie amount collected aftet 10 seconds
        cookie_amount= int(driver.find_element(by=By.ID, value="money").text)
        print(f"cookie amount {cookie_amount}")

        #get the upgrades you can afford now
        upgrades = driver.find_elements(by=By.CSS_SELECTOR, value="#store b")

        upgrade_amounts_dict = {}
        upgrade_list=[]
        for i in upgrades:
            upgrade_amounts= i.text
            if(upgrade_amounts != ""):
                new_amount= int(upgrade_amounts.split("-")[1].strip().replace(",",""))
                temp = {new_amount:upgrade_amounts.split("-")[0].strip()}
                upgrade_amounts_dict.update(temp)
                upgrade_list.append(new_amount)
        print(upgrade_list)
        print(upgrade_amounts_dict)    

        #check for the maximum upgrade

        for i in range(len(upgrade_list)-1,0,-1):
            print(i)
            upnewitem="buy"+upgrade_amounts_dict[upgrade_list[i]]
            upitem = driver.find_element(By.ID, value = upnewitem)
            print(f"clicking and buying the upgrade {upnewitem}")
            print(f"and it has amount {upgrade_list[i]}")
            upitem.click()
            cookie_amount = cookie_amount-upgrade_list[i]
        
        timeout = time.time() + 5



                      

    
