from selenium import webdriver
from time import sleep
from password import pw

#Specify path of your Chrome Driver
chromedriver = "C:\Selenium\chromedriver"

def getcredentials() :
    username = input("Enter Username >> ")
    password = input("Enter Password >> ")
    return username, password

def login(username,password) :
    driver.get("https://www.instagram.com/")
    sleep(2)
    driver.find_element_by_xpath("//input[@name='username']")\
        .send_keys(username)
    driver.find_element_by_xpath("//input[@name='password']")\
        .send_keys(password)
    driver.find_element_by_xpath("//div[contains(text(),'Log In')]")\
        .click()
    sleep(4)

    driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
        .click()

username, password = getcredentials()
driver = webdriver.Chrome(chromedriver)
login(username, password)