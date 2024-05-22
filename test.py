from pytube import YouTube

def download_youtube_video(url, output_path='.'):
    try:
        yt = YouTube(url)
        print(f"Title: {yt.title}")
        print(f"Number of views: {yt.views}")
        ys = yt.streams.get_highest_resolution()
        print(f"Downloading {yt.title}...")
        ys.download(output_path)
        print(f"Download completed! Video saved to {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

url = 'https://youtu.be/8UVNT4wvIGY?autoplay=1'
output_path = '.'
download_youtube_video(url, output_path)