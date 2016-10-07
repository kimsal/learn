
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

file=open("result/datas.csv","w")
file.write("Name;Email\n")
file=open("result/datas.csv","a")
def init_driver():
    driver = webdriver.Firefox()
    return driver
def lookup(driver):
    try:
        driver.get("https://play.google.com/store")
        #scroll bottom
        while True:
            print "go bottom ->"
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
            print str(len(driver.find_elements_by_css_selector("#show-more-button")))
            # if len(driver.find_elements_by_css_selector("#show-more-button"))<=0:
            #     driver.find_elements_by_css_selector("#show-more-button").click()
            #     time.sleep(3)
            driver.find_element_by_css_selector("#show-more-button").click()
            time.sleep(3)

        #get all more link

        #get all app link

        # all_mores= driver.find_elements_by_css_selector("")
        
        file.close()
        #fs.close()
        driver.close()
        print "Process Finished Successfully"
    except TimeoutException:
        print("error ")
if __name__ == "__main__":
    driver = init_driver()
    lookup(driver)
    time.sleep(5)
    driver.quit()