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
from moviepy.video.io.VideoFileClip import VideoFileClip
import yt_dlp

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

    time.sleep(4)
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

def download_youtube_video(output_path=Data.PATH_YOUTUBE):
    from pytube import YouTube
    video = driver.find_element(By.XPATH, "//article//a[@target]")

    url = video.get_attribute('href')
    print(url)
    try:
        ydl_opts = {
            'outtmpl': f'{output_path}/input.mp4',
            'format': 'best'
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception as e:
        print(e)

def download_vid():
    time.sleep(3)
    pyperclip.copy(Data.PATH + "input.mp4")
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('enter')

    actions.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()


def crop_middle_30_seconds(output_file):
    print(output_file)
    clip = VideoFileClip(Data.PATH_YOUTUBE + "\\input.mp4")

    duration = clip.duration

    middle_start = (duration - 30) / 2
    middle_end = middle_start + 30
    cropped_clip = clip.subclip(middle_start, middle_end)
    cropped_clip.write_videofile(Data.PATH+"input.mp4", codec="libx264")
    clip.close()
    cropped_clip.close()




def teardown():
    time.sleep(5)
    driver.quit()