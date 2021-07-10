"""
from pytube import Playlist
import pytube

itemlist = {}

playlist = Playlist("")
for item in playlist:
    j = pytube.YouTube(item).title.title()
    oi = pytube.YouTube(item).metadata.metadata
    print(oi)
    print(j)
    itemlist[j] = [item, oi]

print(itemlist)
from mutagen.easyid3 import EasyID3

audio = EasyID3("example.mp3")
audio['title'] = u"Example Title"
audio['artist'] = u"Me"
audio['album'] = u"My album"
audio['composer'] = u"" # clear
audio.save()
"""
import re
import os
from mutagen.easyid3 import EasyID3
universal_folder = r"D:\Pycharm\PycharmProjects\AHHHHHHHH\DM"

nld = []
os.chdir(universal_folder)
for song in os.listdir(universal_folder):
    audio = EasyID3(song)
    audio['title'] = song.replace(".mp3", "")
    audio['artist'] = u"Panic! At The Disco"
    audio['album'] = u"A Fever You Can't Sweat Out"
    audio['composer'] = u""
    audio.save()
    print(song)
