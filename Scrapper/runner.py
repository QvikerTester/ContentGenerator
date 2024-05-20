from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import win32com.client as comclt
from selenium.webdriver.common.keys import Keys
import Data
import time
import pyautogui
import pyperclip

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
actions = ActionChains(driver)
# driver.manage().window().maximize()

driver.get(Data.URL)

wait = WebDriverWait(driver, 20)

btn = driver.find_element(By.XPATH, "//span[@class = 'Search_magnifyingGlass__uhryW']")
btn.click()

input = driver.find_element(By.XPATH, "//input[@type='text']")
input.send_keys("Song")

time.sleep(2)
first_song = driver.find_elements(By.XPATH, "//div[@role='listbox']//a")
first_song[0].click()


time.sleep(2)
video = driver.find_element(By.XPATH, "//video")
location = video.location
size = video.size

x= location['x']
y= location['y']
print(x, y)
actions.move_by_offset(x, y).context_click().perform()

wsh= comclt.Dispatch("WScript.Shell")
ActionChains(driver).move_to_element(video).context_click().perform()
wsh.SendKeys("{DOWN}")
wsh.SendKeys("{DOWN}")
wsh.SendKeys("{DOWN}")
wsh.SendKeys("{DOWN}")
wsh.SendKeys("{DOWN}")
wsh.SendKeys("{ENTER}")# send the keys you want

time.sleep(5)
pyperclip.copy("C:/Users/Mawan/PycharmProjects/ContentGenerator/Videos/video")
time.sleep(1)
pyautogui.hotkey('ctrl', 'v')

actions.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()



time.sleep(0.5)
