from os import listdir
import subprocess

directory = './tracks/'
mp3_files = [ f for f in listdir(directory) if f[-4:] == '.mp3' ]

if len(mp3_files) == 0:
    print("No mp3 files found!")

process = subprocess.Popen(['mpg123', directory + mp3_files[0]])
