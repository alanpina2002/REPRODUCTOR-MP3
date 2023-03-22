from tkinter import *
import pygame,sys
from pygame.locals import *
from tkinter import filedialog
from PIL import ImageTk, Image


raiz = Tk()
raiz.title("Reproductor Mp3 - GUI")
#raiz.iconbitmap("LED.ico")
raiz.geometry("600x400")
raiz.resizable(1,1)

pygame.init() #este metodo inicia la libreria pygame

def opensong():
    song = filedialog.askopenfilename()
    print("song")
    pygame.mixer.music.load(song)
    

def playsong():
    pygame.mixer.music.play()

def stopsong():
    pygame.mixer.music.stop()

def resumesong():
    pygame.mixer.music.unpause()

def pausesong():
    pygame.mixer.music.pause()

def volumedown():
    nivelVolumen = pygame.mixer.music.get_volume() - 0.5
    pygame.mixer.music.set_volume(nivelVolumen)

def volumeup():
    nivelVolumen = pygame.mixer.music.get_volume() + 0.5
    pygame.mixer.music.set_volume(nivelVolumen)


#frame o marco
framePrincipal = Frame(raiz, bg ="#4d4d4d", width=600, height=400)
framePrincipal.pack(fill="both", expand=1)

imagenchida = Image.open("HOMERO.JPG")
imagenReproductor = imagenchida.resize((200,150))
img = ImageTk.PhotoImage(imagenReproductor)

#titulo imagen
tituloImagen = Label(framePrincipal, image=img)
tituloImagen.pack()

#titulo reproductor
tituloreproductor = Label(framePrincipal, text="Reproductor GUI", bg="#4d4d4d", fg="#f4f4f4", font=("Roboto", 14))
tituloreproductor.place(relx=0.38, rely=0.4)

#botonopenfile
botonopenfile = Button(framePrincipal, text = "Open File" , font=("Roboto", 14, "bold"), bg="#5dc460", fg="#f4f4f4", width=10, height=2,
bd = 0, highlightthickness=0, comand = opensong)
botonopenfile.place(relx=0, rely=0.5)

#botonplaysong
botonplaysong = Button(framePrincipal, text = "Play Song" , font=("Roboto", 14, "bold"), bg="#5dc460", fg="#f4f4f4", width=10, height=2,
bd = 0, highlightthickness=0, command = playsong)
botonplaysong.place(relx=0.2, rely=0.5)

#botonstop
botonstop = Button(framePrincipal, text = "Stop" , font=("Roboto", 14, "bold"), bg="#e2504c", fg="#f4f4f4", width=10, height=2,
bd = 0, highlightthickness=0)
botonstop.place(relx=0.4, rely=0.5, command = stopsong)

#botonresume
botonresume = Button(framePrincipal, text = "Resume" , font=("Roboto", 14, "bold"), bg="#ffc400", fg="#f4f4f4", width=10, height=2,
bd = 0, highlightthickness=0)
botonresume.place(relx=0.6, rely=0.5, command = resumesong)

#botonpause
botonpause = Button(framePrincipal, text = "Pause" , font=("Roboto", 14, "bold"), bg="#e2504c", fg="#f4f4f4", width=10, height=2,
bd = 0, highlightthickness=0)
botonpause.place(relx=0.8, rely=0.5, command = pausesong)

#botonvolumeup
botonvolumeup = Button(framePrincipal, text = "volumeup" , font=("Roboto", 14, "bold"), bg="#e2504c", fg="#f4f4f4", width=10, height=2,
bd = 0, highlightthickness=0)
botonvolumeup.place(relx=0.4, rely=0.7, command = volumeup)

#botonvolumedown
botonvolumedown = Button(framePrincipal, text = "volumedown" , font=("Roboto", 14, "bold"), bg="#e2504c", fg="#f4f4f4", width=10, height=2,
bd = 0, highlightthickness=0)
botonvolumedown.place(relx=0.6, rely=0.7, command = volumedown)

raiz.mainloop()