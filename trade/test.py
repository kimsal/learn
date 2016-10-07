# Python selenium 
# intermarchedrive
# Create By amok Team
# Created on: 07-02-2016
#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
job_list=[]
def init_driver():
    driver = webdriver.Firefox()
    return driver
def lookup(driver):
    try:
        driver.get("https://poloniex.com/login")
        driver.find_element_by_id('input[name="username"]').send_keys("kimsalsan007@gmail.com")
        driver.find_element_by_id('input[name="password"]').send_keys("11101999sal")
        driver.close()
        print "Process Finished Successfully"
    except TimeoutException:
        print("error ")
if __name__ == "__main__":
    driver = init_driver()
    lookup(driver)
    time.sleep(5)
    driver.quit()