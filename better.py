# import ytplpy.main
from pytube import YouTube

# ytplpy.main.downloadmp3playlist("")
song = ""

YouTube(song).streams.first().download()
