from Scrapper import Step
import time

def automation(song_name):
    driver, actions = Step.config_chrome()
    Step.open_url()
    Step.search_song(song_name)
    try:
        print("IN TRY")
        Step.open_vid_context()
        time.sleep(4)
        print("VID CONTEXT OPENED")
        Step.download_vid()
        print("VID DOWNLOADED")
        Step.teardown()
        return True
    except:
        print("EXCEPT STARTED")
        time.sleep(4)
        Step.download_youtube_video()
        # print("YOUTUBE VID DOWNLOADED")
        # time.sleep(15)
        # Step.crop_middle_30_seconds(song_name)
        Step.teardown()
        return False

