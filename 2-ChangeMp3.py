import os
from moviepy.editor import *
import glob

lista_mp4 = glob.glob('*.mp4')

print(lista_mp4)

for video in lista_mp4:
    print("Lendo arquivo Mp4")
    print('-'*20)
    mp4 = VideoFileClip(os.path.join(video))
    nome_mp3 = video [:-4] + '.mp3'

    print("Convertendo para mp3")
    mp4.audio.write_audiofile(os.path.join(nome_mp3))
    print('-'*20)
    print('Converteu para mp4' + video + 'para mp3' + nome_mp3 )