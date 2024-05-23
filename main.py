from Scrapper import automation_runner
from Scrapper import songs_reader
from Editor import video_editor

songs = songs_reader.read_songs()

for song in songs:
    if songs_reader.duplicate_remover(song)!=True:
        try:
            print(song)
            automation_runner.automation(song)
            video_editor.edit_video(song)
            songs_reader.add_song_title(song)
        except:
            print("UNEXPECTED SHIT HAPPENED")
