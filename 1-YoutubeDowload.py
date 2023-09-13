from pytube import YouTube

link =  str (input("Cole o link desejado: "))

yt = YouTube(link)
print("Estamos baixando o seu vídeo. Aguarde...")
stream = yt.streams.get_highest_resolution()
stream.download()

print("Video baixado !!!")
#Fim
