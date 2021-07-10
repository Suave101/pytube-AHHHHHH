# import ytplpy.main
from pytube import YouTube

# ytplpy.main.downloadmp3playlist("https://www.youtube.com/playlist?list=PLkCV0SkyKAS3DnlTLvWrpeoCsMo4zB-bF")
song = "https://www.youtube.com/watch?v=cNcv81GP0E4&list=PL84xFETGL4aeT2RvHcr6vXKXwE7_nVZv7&index=14"

YouTube(song).streams.first().download()
