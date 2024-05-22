import yt_dlp

def download_youtube_video(url, output_path='.'):
    ydl_opts = {
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'format': 'best'
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

url = "https://youtu.be/3wkNLqetX0M?autoplay=1"
output_path = "."  # Specify your output path here
download_youtube_video(url, output_path)