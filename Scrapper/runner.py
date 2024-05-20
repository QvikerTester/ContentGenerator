import Step

driver, actions = Step.config_chrome()

Step.open_url()

Step.search_song()

Step.open_vid_context()

Step.download_vid()
