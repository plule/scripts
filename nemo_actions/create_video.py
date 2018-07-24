#!/usr/bin/python3
# Usage: create_video.py <folder> <audio_file> <picture_file>

import sys
import os
import subprocess

def exit_pause():
    input("Press any key to exit.")
    exit()

def exit_usage():
    print("A picture and an audio file must be selected.")
    exit_pause()

def is_audio(f):
    name, ext = os.path.splitext(f)
    return ext.lower() in [".mp3",".ogg",".wav"]

def is_picture(f):
    name, ext = os.path.splitext(f)
    return ext.lower() in [".jpg", ".jpeg", ".bmp", ".png"]

if len(sys.argv) != 4:
    exit_usage()

folder = sys.argv[1]
audio_file = None
picture_file = None

if is_audio(sys.argv[2]):
    audio_file = sys.argv[2]
elif is_picture(sys.argv[2]):
    picture_file = sys.argv[2]

if is_audio(sys.argv[3]):
    audio_file = sys.argv[3]
elif is_picture(sys.argv[3]):
    picture_file = sys.argv[3]

if audio_file is None or picture_file is None:
    exit_usage()

audio_file_name, audio_file_ext = os.path.splitext(audio_file)
video_file = os.path.join(folder, audio_file_name + ".mkv")

#print folder
print("audio: " + audio_file)
print("picture: " + picture_file)
print("video: " + video_file)

args = [
    "ffmpeg",
    "-loop", "1",
    "-i", picture_file,
    "-i", audio_file,
    "-shortest",
    "-tune", "stillimage",
    "-c:v", "libx264",
    "-c:a", "copy",
    video_file
]

print(subprocess.list2cmdline(args))
subprocess.run(args)
exit_pause()
