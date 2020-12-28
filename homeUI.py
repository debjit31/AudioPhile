import tkinter as tk
import os
import tkinter.messagebox as tkMessageBox
from tkinter import font
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from converter import AudioFile

root  = tk.Tk()
canvas = tk.Canvas(root, height = 200, width = 650)
canvas.pack()
root.title('AudioPhile')


def open_file():
    file = askopenfile(mode ='r', filetypes =[('Text Files', '*.txt')])
    if file is not None:
        slabelAddr['text'] = file.name
        af.getSourceFile(file.read(), file.name)

def store_directory():
    target = filedialog.askdirectory()
    dlabelAddr['text'] = target
    addr = target+'/AudioFiles'
    af.getDestination(addr)

def make_audio():
   af.makeAudioBook()
   tkMessageBox.showinfo("Success", "Audio Book Generated......")

if __name__ == "__main__":
    slabel = tk.Label(root, text = 'Source File', font = ('Courier', 10))
    slabel.place(anchor = 'n', relx=0.10, rely=0.09, relheight = 0.15, relwidth=0.2)
    slabelAddr = tk.Label(root,bg = '#ffffff', font=('Courier', 9))
    slabelAddr.place(anchor = 'n', relx=0.48, rely=0.09, relheight = 0.15, relwidth=0.6)
    sButton = tk.Button(root, text = 'Browse', font=('Courier', 11), command = lambda : open_file())
    sButton.place(anchor = 'n', relx=0.88, rely=0.09, relheight = 0.15, relwidth=0.15)


    dlabel = tk.Label(root, text = 'Destination', font = ('Courier', 10))
    dlabel.place(anchor = 'n', relx=0.10, rely=0.4, relheight = 0.15, relwidth=0.2)
    dlabelAddr = tk.Label(root,bg = '#ffffff', font=('Courier', 9))
    dlabelAddr.place(anchor = 'n', relx=0.48, rely=0.4, relheight = 0.15, relwidth=0.6)
    dButton = tk.Button(root, text = 'Browse', font=('Courier', 11), command=lambda:store_directory())
    dButton.place(anchor = 'n', relx=0.88, rely=0.4, relheight = 0.15, relwidth=0.15)

    genBtn = tk.Button(root, text = 'Generate Audio File', font=('Courier', 11), command = lambda: make_audio())
    genBtn.place(anchor = 'n', relx=0.5, rely=0.65, relheight = 0.15, relwidth=0.35)

    af = AudioFile()
    root.mainloop()
