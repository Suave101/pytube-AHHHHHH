import os

os.chdir("Download")
ld = os.listdir()
nld = []
print(ld)
for song in ld:
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
