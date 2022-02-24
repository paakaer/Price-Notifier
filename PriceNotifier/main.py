# selenium 4
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options as FirefoxOptions

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
options = FirefoxOptions()
driver = webdriver.Firefox(options=options)

driver.quit()
