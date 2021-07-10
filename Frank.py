from pytube import YouTube
from pytube import Playlist
from pytube import extract
import os
import moviepy.editor as mp
import re
import time
# Try that
"pip install audioplayer"

while True:
    try:
        while True:
            t = 0
            playlist = Playlist("")
            for url in playlist:
                t = 0 + 1
                YouTube(url).streams.get_highest_resolution().download(r"C:\\")
                time.sleep(0.3)
                print("Video Downloaded")
                print(f"Items Printed: {str(t)}")
            j = os.listdir(path=r"C:\\")
            if len(j) >= t:
                break
            print("Downloaded?")
        folder = r"C:\\"
        """
                for file in os.listdir(universal_folder):
            if re.search('mp4', file):
                mp4_path = os.path.join(universal_folder, file)
                mp3_path = os.path.join(universal_folder, os.path.splitext(file)[0] + '.mp3')
                new_file = mp.AudioFileClip(mp4_path)
                new_file.write_audiofile(mp3_path)
                os.remove(mp4_path)
        """
        break
    except Exception as e:
        print(e)
