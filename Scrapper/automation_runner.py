from Scrapper import Step
import time

def automation(song_name):
    driver, actions = Step.config_chrome()
    Step.open_url()
    Step.search_song(song_name)
    try:
        Step.open_vid_context()
        time.sleep(4)
        Step.download_vid()
        Step.teardown()
        return True
    except:
        time.sleep(4)
        Step.download_youtube_video()
        time.sleep(15)
        Step.crop_middle_30_seconds(song_name)
        Step.teardown()
        return False

