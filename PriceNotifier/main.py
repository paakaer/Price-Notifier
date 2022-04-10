from selenium import webdriver
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from PIL import Image
from pytesseract import pytesseract
i = 0
if __name__ == "__main__":
    def main():
        fileName = "Stores.json"
        driver = webdriver.Firefox(executable_path="/home/paakaer/PycharmProjects/PriceNotifier/drivers/geckodriver")
        firstTab = driver.current_window_handle
        fileData = fileLoading(fileName)
        tabInitializer(driver, fileData)
        time.sleep(11)
        driver.quit()


    def fileLoading(fileName):
        with open(fileName, 'r') as file:
            fileData = json.load(file)
        return fileData

    def tabInitializer(tabHandler, fileData):
        sID = ["edit-search-term",
               "inputSearch",
               "searchText"]
        kw = "Oppo reno 6 pro"
        for link in fileData["Amazon"]:
            tabHandler.get(link)
            amazonKeywordSearcherByID(kw, tabHandler, "twotabsearchtextbox")
            screenShot(tabHandler)
            #getData(tabHandler, kw, "prova.txt", link)
            tabHandler.switch_to.new_window("tab")
        for link in fileData["Ebay"]:
            tabHandler.get(link)
            keywordSearcherByID(kw, tabHandler, "gh-ac")
            screenShot(tabHandler)
            tabHandler.switch_to.new_window("tab")
        for link, sBar in zip(fileData["BrickAndMortar"], sID):
            tabHandler.get(link)
            keywordSearcherByID(kw, tabHandler, sBar)
            screenShot(tabHandler)
            tabHandler.switch_to.new_window("tab")

    def amazonKeywordSearcherByID(keyword, driver, searchBarID):
        searchBar = driver.find_element(By.ID, searchBarID)
        searchBar.send_keys(keyword + Keys.ENTER)
        try:
            cookieAccept = driver.find_element(By.ID, "sp-cc-accept")
            cookieAccept.click()
        finally:
            print("cookie id not found in " + driver.current_url)
            # searchButton = driver.find_element(By.ID, "nav-search-submit-button")


    def keywordSearcherByID(keyword, driver, searchBarID):
        searchBar = driver.find_element(By.ID, searchBarID)
        searchBar.send_keys(keyword + Keys.ENTER)

    def itemSelectionAmazon(keyword, driver, itemTag):
        itemDescription = driver.find_elements(By.CLASS_NAME, "a-size-base-plus")
        for q in itemDescription:
            if keyword in q.text:
                print(driver.find_element(By.CLASS_NAME, "a-price-whole").text)
            #print(itemPrice)
        '''else:
            print(q.text)'''

    def screenShot(driver):
        time.sleep(9.8)
        driver.save_screenshot("images/image({}).png".format(i))
        ++i

main()
'''
    #Amazon - 
        <div class="a-section a-spacing-base">
        /html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div[3]/div/div/div/div/div/div
        /html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div[3]/div/div/div/div/div/div/div[2]/div[1]/h2/a/span
        
        /html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div[4]/div/div/div/div
        /html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div[4]/div/div/div/div/div[2]/div[1]/h2/a/span
'''