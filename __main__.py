import argparse
from pytube import YouTube
from pytube.exceptions import RegexMatchError
from moviepy.editor import AudioFileClip

parser = argparse.ArgumentParser(description="Download video/audio from Youtube")

parser.add_argument('youtube_link', metavar='url', type=ascii, help="Youtube URL link")
parser.add_argument('--audio', action='store_true', help="Only download audio")
parser.add_argument('--filename', help="Rename the downloaded file")

args = parser.parse_args()


# Global variable
DOWNLOADED_VIDEO_FILE_PATH = "DownloadedVideo"


def download_video(youtube_stream):
    return youtube_stream.download(output_path=DOWNLOADED_VIDEO_FILE_PATH, filename=args.filename)

try:
    yt_obj = YouTube(args.youtube_link)
    print("Video found. Downloading the video now.")

    if args.audio:
        # Download Youtube file
        filters = yt_obj.streams.filter(only_audio=True)    
        download_video(filters[0])

        print("Video finish downloaded")

        # Convert to MP3
        print("Converting to MP3 now....")

        audio_clip = AudioFileClip(f"{DOWNLOADED_VIDEO_FILE_PATH}/{args.filename or yt_obj.title}.mp4")
        audio_clip.write_audiofile(f"{DOWNLOADED_VIDEO_FILE_PATH}/{args.filename or yt_obj.title}.mp3")
        audio_clip.close()
        print("Finish converted")

    else:
        # progressive=True mean that stream have both video & audio
        filters = yt_obj.streams.filter(progressive=True)

        download_video(filters.get_highest_resolution())
        print("Video finish downloaded")  

except RegexMatchError as e:
    print("Unable to find the Youtube video.")
    print("Probably is a private video.")

except Exception as e:
    print(e)
    print("Youtube available stream:")
    print("===============================")
    print(yt_obj.streams)
