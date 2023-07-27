import tkinter as tk
from tkinter import simpledialog
from ScreenRecorder import ScreenRecorder
from audio import record_audio


def start_screen_recording():
    t=0
    input_dialog = tk.simpledialog.askinteger("Recording Duration", "Enter the recording duration in seconds:")
    if input_dialog is not None:
       t= input_dialog
    ScreenRecorder(t)
def start_audio_recording():
    t=0
    input_dialog = tk.simpledialog.askinteger("Recording Duration", "Enter the recording duration in seconds:")
    if input_dialog is not None:
       t= input_dialog
    record_audio(t)
window = tk.Tk()

window.title("AVP RECODER")
window.geometry("600x400")
window.configure(bg="tomato")

text = tk.Label(window, text="WELCOME!", bg="TOMATO", font=('arial black', 20))
text.pack(pady=20)

text = tk.Label(window, text="Welcome to AVP Devlopment", bg="tomato", font=('century', 15))
text.pack(pady=5)

button2 = tk.Button(window, text="ScreenRecoder", font=("century", 10), bg="pink",command=start_screen_recording)
button2.place(width=500, height=100)
button2.config(width=30, height=2)
button2.pack(pady=10)

button3 = tk.Button(window, text="Audio Recorder", font=("century", 10), bg="pink",command=start_audio_recording)
button3.place(width=500, height=100)
button3.config(width=30, height=2)
button3.pack(pady=10)

window.mainloop()