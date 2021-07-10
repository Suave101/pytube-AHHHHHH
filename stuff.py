from pytube import YouTube
from pytube import Playlist
from pytube import extract
import os
import moviepy.editor as mp
import re
import time
# Try that
"pip install audioplayer"
universal_folder = r"D:\Pycharm\PycharmProjects\AHHHHHHHH\Download"

while True:
    try:
        while True:
            t = 0
            playlist = Playlist("")
            print(playlist)
            for url in playlist:
                t = 1 + t
                print(f"Current URL Downloading: {url}")
                YouTube(url).streams.get_audio_only().download(universal_folder)
                time.sleep(0.3)
                print(f"Song Download Complete: {url}")
                print(f"Songs Downloaded: {t}")
            j = os.listdir(path=universal_folder)
            if len(j) >= t:
                break
        print("Songs Downloaded Successfully")
        print("File Conversion Initiated")
        files_converted = 0
        for file in os.listdir(universal_folder):
            print(f"Now Converting File {files_converted + 1} of {len(os.listdir(universal_folder))}")
            if re.search('mp4', file):
                mp4_path = os.path.join(universal_folder, file)
                mp3_path = os.path.join(universal_folder, os.path.splitext(file)[0] + '.mp3')
                new_file = mp.AudioFileClip(mp4_path)
                new_file.write_audiofile(mp3_path)
                os.remove(mp4_path)
            files_converted = files_converted + 1
            print(f"File {files_converted} of {len(os.listdir(universal_folder))} Complete")
        print("Files Successfully Converted")
        print("Renaming of files Init")
        nld = []
        od = os.getcwd()
        os.chdir(universal_folder)
        for song in os.listdir(universal_folder):
            original_song = song
            song = song.lower()
            song = song.replace("bob marley", "")
            song = song.replace("-", "")
            x = 100
            while True:
                song = song.replace("        ", " ")
                song = song.replace("       ", " ")
                song = song.replace("      ", " ")
                song = song.replace("     ", " ")
                song = song.replace("    ", " ")
                song = song.replace("   ", " ")
                song = song.replace("  ", " ")
                song = song.replace("   ", " ")
                song = song.replace("    ", " ")
                song = song.replace("     ", " ")
                song = song.replace("      ", " ")
                song = song.replace("       ", " ")
                song = song.replace("        ", " ")
                song = song.replace("       ", " ")
                song = song.replace("      ", " ")
                song = song.replace("     ", " ")
                song = song.replace("    ", " ")
                song = song.replace("   ", " ")
                song = song.replace("  ", " ")
                song = song.replace("   ", " ")
                song = song.replace("    ", " ")
                song = song.replace("     ", " ")
                song = song.replace("      ", " ")
                song = song.replace("       ", " ")
                song = song.replace("        ", " ")
                song = song.replace("        ", " ")
                song = song.replace("       ", " ")
                song = song.replace("      ", " ")
                song = song.replace("     ", " ")
                song = song.replace("    ", " ")
                song = song.replace("   ", " ")
                song = song.replace("  ", " ")
                if x < 1:
                    break
                else:
                    x = x - 1
            song = song.replace("(lyrics)", "")
            song = song.replace("(original)", "")
            song = song.replace("(from the legend album with lyrics)", "")
            song = song.replace("(letra inglés)", "")
            song = song.strip()
            song = song.title()
            song = song.replace(".Mp3", ".mp3")
            song = song.replace(" .mp3", ".mp3")
            os.rename(original_song, song)
            nld.append(song)
        print(nld)
        os.chdir(od)
        break
    except Exception as e:
        print(e)
