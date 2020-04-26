from selenium import webdriver
from time import sleep
from password import pw
from Login import getcredentials, login, driver


def AcceptRequests() :
    driver.find_element_by_xpath("//div[4]//a[1]//*[local-name()='svg']")\
        .click()
    sleep(2)

    if driver.find_element_by_xpath("//div[@class='PUHRj eKc9b H_sJK']//div[@class='YFq-A']") :
        driver.find_element_by_xpath("//div[@class='PUHRj eKc9b H_sJK']//div[@class='YFq-A']")\
            .click()
        sleep(2)

    while 1 :
        if driver.find_element_by_xpath("//button[contains(text(),'Confirm')]") :
            driver.find_element_by_xpath("//button[contains(text(),'Confirm')]")\
                .click()
            sleep(2)


AcceptRequests()