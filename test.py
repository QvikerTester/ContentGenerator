from pytube import YouTube

def download_youtube_video(url, output_path='.'):
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()
    stream.download(output_path)
    print(f"Downloaded: {yt.title}")


url = "https://youtu.be/uIBJJ3M76Mg?autoplay=1"
output_path = "."  # Specify your output path here
download_youtube_video(url, output_path)