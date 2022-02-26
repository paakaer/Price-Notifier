from selenium import webdriver
import json

def tabInitializer(tabHandler):
    for link in fileData["Amazon"]:
        tabHandler.get(link)
        driver.switch_to.new_window("tab")
    for link in fileData["Ebay"]:
        tabHandler.get(link)
        driver.switch_to.new_window("tab")


with open("Stores.json", 'r') as file:
    fileData = json.load(file)

driver = webdriver.Firefox(executable_path="/home/paakaer/PycharmProjects/PriceNotifier/drivers/geckodriver")
tabInitializer(driver)

driver.quit()
