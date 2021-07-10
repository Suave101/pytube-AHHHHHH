import re
import os
universal_folder = r"D:\Pycharm\PycharmProjects\AHHHHHHHH\DM"

nld = []
os.chdir(universal_folder)
for song in os.listdir(universal_folder):
	print(song)
	original_song = song
	song = song.lower()
	song = song.replace("panic! at the disco", "")
	song = song.replace("[official video]", "")
	song = song.replace("-", "")
	song = song.replace("  ", "")
	song = song.replace("   ", "")
	song = song.replace("    ", "")
	song = song.replace("     ", "")
	song = song.replace("      ", "")
	song = song.replace("       ", "")
	song = song.replace("        ", "")
	song = song.replace(" [Official Video]", "")
	song = re.sub(r"\([^()]*\)", "", song)
	song = song.strip()
	song = song.title()
	song = song.replace(" .Mp3", ".mp3")
	song = song.replace(".Mp3", ".mp3")
	os.rename(original_song, song)
	nld.append(song)
print(nld)
