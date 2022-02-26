from selenium import webdriver
import json

def tabInitializer(tabHandler):
    for link in fileData["Amazon"]:
        tabHandler.get(link)
        driver.switch_to.new_window("tab")
    for link in fileData["Ebay"]:
        tabHandler.get(link)
        driver.switch_to.new_window("tab")


# print(fileData["Amazon"]["Amazon Italia"])

with open("Stores.json", 'r') as file:
    fileData = json.load(file)

driver = webdriver.Firefox(executable_path="/home/paakaer/PycharmProjects/PriceNotifier/drivers/geckodriver")
tabInitializer(driver)
'''originalWindow = driver.current_window_handle
tabInitializer(originalWindow)
driver.switch_to.new_window("tab")
driver.get(fileData["Amazon"]["Amazon Italia"])
for site in fileData["Ebay"]:
    driver.switch_to.new_window("tab")
    driver.get(site["url"])
# driver.get("")
# driver.switch_to.new_window('tab')

tabInitializer(driver)
'''
driver.quit()
