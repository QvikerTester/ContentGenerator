from Scrapper import Step

def automation(song_name):
    driver, actions = Step.config_chrome()
    Step.open_url()
    Step.search_song(song_name)
    try:
        Step.open_vid_context()
        Step.download_vid()
        Step.teardown()
        return True
    except:
        Step.download_youtube_video()
        Step.teardown()
        return False

