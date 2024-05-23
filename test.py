from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import csv

def config_chrome():
    global driver, actions
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    actions = ActionChains(driver)

    return driver, actions

def open_url():
    driver.get("https://www.shazam.com/charts/genre/world/electronic")


def get_names():
    data=[[]]
    arr = []
    try:
        box = driver.find_elements(By.XPATH, "//a[@class='ContainerLink-module_containerLinkElement__EOJ6S common_link__7If7r']")
        for name in box:
            arr.append(name.get_attribute("aria-label"))
            data[0].append(1)
            print(name.get_attribute("aria-label")+",")
    except:
        print("Skip")
    df=pd.DataFrame(data, columns=arr)
    df.to_csv("songs_techno.csv",  index=False)


config_chrome()
open_url()
get_names()