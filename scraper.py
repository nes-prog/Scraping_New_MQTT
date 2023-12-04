from selenium import webdriver 
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys 
 #initialize chromedriver for scraping
DRIVER_PATH = 'chromedriver.exe'
GOOGLE_news = 'https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp1ZEdvU0FtWnlHZ0pHVWlnQVAB?hl=fr&gl=FR&ceid=FR%3Afr'

def scrape():
    "Scrape News from the google news url"
    # initialize webdriver
    driver = webdriver.Chrome(DRIVER_PATH)
    # get the url for scraping
    driver.get(GOOGLE_news)
    sleep(2)
    button = driver.find_element(By.XPATH, '/html/body/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/div[1]/form[1]/div/div/button')
    button.click()
    #scrape news
    blocks = driver.find_elements(By.CLASS_NAME, 'WwrzSb')
    return blocks
