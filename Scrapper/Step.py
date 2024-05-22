from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import win32com.client as comclt
from selenium.webdriver.common.keys import Keys
from Scrapper import Data
import time
import pyautogui
import pyperclip
import uuid


def config_chrome():
    global driver, actions
    options = webdriver.ChromeOptions()
    # options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options)
    actions = ActionChains(driver)

    return driver, actions

def open_url():
    driver.get(Data.URL)


def search_song(song_name):
    btn = driver.find_element(By.XPATH, "//span[@class = 'Search_magnifyingGlass__uhryW']")
    btn.click()

    input = driver.find_element(By.XPATH, "//input[@type='text']")
    input.send_keys(song_name)

    time.sleep(2)
    first_song = driver.find_elements(By.XPATH, "//div[@role='listbox']//a")
    first_song[0].click()

def open_vid_context():
    global video
    time.sleep(2)
    video = driver.find_element(By.XPATH, "//video")
    location = video.location
    size = video.size

    x = location['x']
    y = location['y']
    print(x, y)
    actions.move_by_offset(x, y).context_click().perform()
    wsh = comclt.Dispatch("WScript.Shell")
    ActionChains(driver).move_to_element(video).context_click().perform()

    wsh.SendKeys("{DOWN}")
    wsh.SendKeys("{DOWN}")
    wsh.SendKeys("{DOWN}")
    wsh.SendKeys("{DOWN}")
    wsh.SendKeys("{DOWN}")
    wsh.SendKeys("{ENTER}")

def download_vid():
    time.sleep(3)
    pyperclip.copy(Data.PATH+ "input.mp4")
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('enter')

    actions.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()

def teardown():
    time.sleep(5)
    driver.quit()