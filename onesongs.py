from pytube import YouTube
import os
import moviepy.editor as mp

universal_folder = os.getcwd()

url = "https://www.youtube.com/watch?v=G2g3zfHqW4Q&list=PLkCV0SkyKAS1S5qAsXXEj7PY4MZ1xyCsI&index=1"
YouTube(url).streams.get_highest_resolution().download()
file = YouTube(url).title.title().replace("/", "") + ".mp4"
print(file)
mp4_path = os.path.join(universal_folder, file)
mp3_path = os.path.join(universal_folder, os.path.splitext(file)[0] + '.mp3')
new_file = mp.AudioFileClip(mp4_path)
new_file.write_audiofile(mp3_path)
os.remove(mp4_path)
