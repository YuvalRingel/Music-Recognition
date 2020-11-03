from scipy.io import wavfile
from pytube import YouTube
import matplotlib.pyplot as plt
import os
import subprocess


# tdl
# Youtube

# doesnt work...
def download_sound(link):
    yt = YouTube(link)
    t = yt.streams.filter(only_audio=True).all()
    name = 'testing'  # naming
    path = './downloaded/'
    t[0].download(output_path=path, filename=name)
    old_file = path + name + '.mp4'
    new_file = path + name + '.wav'

    # MAGIC
    command = "C:/ffmpeg/bin/ffmpeg -i "+ old_file+ " -ab 160k -ac 2 -ar 44100 -vn " + new_file
    subprocess.call(command, shell=True)
    data = load_sound(path=new_file)
    delete_file(old_file)
    delete_file(new_file)
    return data


def load_sound(path):
    samplerate, data = wavfile.read(path)
    #data = data[(len(data) // 64) - 1000:(len(data) // 32)]
    #data = data[700000:2500000]
    # plt.plot(data)
    # plt.show()
    return samplerate, data


def delete_file(file):
    if os.path.exists(file):
            os.remove(file)
    else:
        print("The file does not exist")


