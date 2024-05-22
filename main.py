from Scrapper import automation_runner
from Scrapper import songs_reader
from Editor import video_editor
songs = songs_reader.read_songs()

for song in songs:
    automation_runner.automation(song)
    video_editor.edit_video(song)


