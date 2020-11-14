from pytube import YouTube

youtube_url = input("Kindly enter the Youtube URL:")

try:
    yt_obj = YouTube(youtube_url)

    filters = yt_obj.streams.filter(progressive=True)

    filters.get_highest_resolution().download("Video")

    print("Video finish downloaded")
except Exception as e:
    print(e)
