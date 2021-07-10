import tkinter
from pytube import YouTube
from pytube import Playlist
from pytube import extract
import os
import moviepy.editor as mp
import re
import time
universal_folder = r"C:\\"


def run():
    global universal_folder
    global tk_url
    while True:
        try:
            while True:
                t = 0
                print(tk_url.get())
                print(str(tk_url.get()))
                playlist = Playlist(str(tk_url.get()))
                for url in playlist:
                    t = t + 1
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
            for song in os.listdir(universal_folder):
                original_song = song
                song = song.lower()
                song = song.replace("-", "")
                song = song.replace("  ", " ")
                song = song.replace("   ", " ")
                song = song.replace("    ", " ")
                song = song.replace("     ", " ")
                song = song.replace("      ", " ")
                song = song.replace("       ", " ")
                song = song.replace("        ", " ")
                song = re.sub(r"\([^()]*\)", "", song)
                song = song.replace(" .mp3", ".mp3")
                song = song.strip()
                song = song.title()
                song = song.replace(".Mp3", ".mp3")
                print(original_song)
                print(song)
                od = os.getcwd()
                os.chdir(universal_folder)
                os.rename(original_song, song)
                os.chdir(od)
                nld.append(song)
            print(nld)
            break
        except Exception as e:
            print(e)


root = tkinter.Tk()
root.geometry('400x50')
root.title("Alexanders Amazing YT Downloader")
tk_url = tkinter.StringVar()
box = tkinter.Entry(root, textvariable=tk_url)
button = tkinter.Button(root, text="Submit", command=run)
box.grid(column=1, row=0)
button.grid(column=0, row=0)
root.mainloop()
