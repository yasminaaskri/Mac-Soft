from tkinter import *
from tkinter import ttk
from tkinter import messagebox, ttk
import tkinter as tk
import platform
import psutil
from PIL import Image, ImageTk, ImageSequence
from ctypes import cast, POINTER
from comtypes  import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import screen_brightness_control as sbc

# Colors
bg_color = "#343434"

root = Tk()
root.title("System Information")
root.geometry("850x500+300+150")
root.resizable(False, False)
root.config(bg=bg_color)

# Icon
icon = PhotoImage(file="./images/icon.png")
root.iconphoto(False, icon)

Body = Frame(root, width=900, height=600, bg="#d8e2dc")
Body.pack(pady=20, padx=20)

# PC Info
LHS = Frame(Body, width=310, height=435, bg="#fff", highlightbackground="gray")
LHS.place(x=10, y=10)

# PC photo
photo = PhotoImage(file="./images/pc.png")
myimage = Label(LHS, image=photo)
myimage.place(x=2, y=20)

mysystem = platform.uname()

l1 = Label(LHS, text=mysystem.node, bg="#fff", font=('Acumin Variable Concept', 15, 'bold'), justify="center")
l1.place(x=10, y=200)
l2 = Label(LHS, text=f"Version: {mysystem.version}", bg="#fff", font=('Acumin Variable Concept', 8), justify="center")
l2.place(x=10, y=230)
l3 = Label(LHS, text=f"System: {mysystem.system}", bg="#fff", font=('Acumin Variable Concept', 15), justify="center")
l3.place(x=10, y=260)
l4 = Label(LHS, text=f"Machine: {mysystem.machine}", bg="#fff", font=('Acumin Variable Concept', 15), justify="center")
l4.place(x=10, y=290)
l5 = Label(LHS, text=f"Total RAM installed: {round(psutil.virtual_memory().total / 1000000000, 2)} GB", bg="#fff", font=('Acumin Variable Concept', 15), justify="center")
l5.place(x=10, y=320)
l6 = Label(LHS, text=f"Processor: {mysystem.processor}", bg="#fff", font=('Acumin Variable Concept', 7), justify="center")
l6.place(x=10, y=350)

# Battery Info
RHS = Frame(Body, width=470, height=230, bg="#fff", highlightbackground="gray")
RHS.place(x=330, y=10)

system = Label(RHS, text="System", bg="#fff", font=('Acumin Variable Concept', 15, 'bold'))
system.place(x=10, y=10)

battery_label = Label(RHS, bg="#fff")
battery_label.place(x=15, y=50)

# Load battery images
charging_img = Image.open("./images/charging.gif")
discharging_img = Image.open("./images/image.png")

# Resize frames
charging_img_resized = [ImageTk.PhotoImage(img.resize((100, 100), Image.LANCZOS)) for img in ImageSequence.Iterator(charging_img)]

frame_idx = 0

def convertTime(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d" % (hours, minutes, seconds)

def update_battery_info():
    global frame_idx  # Use global to access the frame_idx variable
    battery = psutil.sensors_battery()
    percent = battery.percent
    time_left = convertTime(battery.secsleft)

    lbl.config(text=f'{percent}%')
    lbl_plugged.config(text=f'Plugged: {str(battery.power_plugged)}')
    lbl_time.config(text=f'Time Left: {time_left}')

    if battery.power_plugged:
        battery_label.config(image=charging_img_resized[frame_idx])
        battery_label.image = charging_img_resized[frame_idx]  # Keep a reference
        frame_idx = (frame_idx + 1) % len(charging_img_resized)
    else:
        battery_img_resized = ImageTk.PhotoImage(discharging_img.resize((100, 100), Image.LANCZOS))
        battery_label.config(image=battery_img_resized)
        battery_label.image = battery_img_resized  # Keep a reference

    lbl.after(100, update_battery_info)

lbl = Label(RHS, bg="#fff", font=('Acumin Variable Concept', 40, 'bold'))
lbl.place(x=200, y=40)

lbl_plugged = Label(RHS, bg="#fff", font=('Acumin Variable Concept', 10))
lbl_plugged.place(x=200, y=100)

lbl_time = Label(RHS, bg="#fff", font=('Acumin Variable Concept', 15))
lbl_time.place(x=200, y=120)

update_battery_info()

############################speaker#############

lbl_speaker = Label(RHS, text="Speaker", bg="#fff", font=('Acumin Variable Concept', 10))
lbl_speaker.place(x=10, y=170)
volume_value=DoubleVar()

def get_current_voluem():
    return '{: .2f}'.format(volume_value.get())

def volume_changed(event):
    device=AudioUtilities.GetSpeakers()
    interface=device.Activate(IAudioEndpointVolume._iid_,CLSCTX_ALL,None)
    volume=cast(interface,POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevelScalar(volume_value.get() / 100, None)

style=ttk.Style()
style.configure("TScale",bg="#fff")
volume=ttk.Scale(RHS,from_=0,to=100,orient=HORIZONTAL,command=volume_changed,variable=volume_value)
volume.place(x=90,y=170)
volume.set(20)

####################brightness####################
lbl_brightness = Label(RHS, text="Brightness", bg="#fff", font=('Acumin Variable Concept', 10))
lbl_brightness.place(x=10, y=200)
brightness_value=DoubleVar()
def get_current_brightness():
    return '{: .2f}'.format(brightness_value.get())

def brightness_changed(event):
   sbc.set_brightness(brightness_value.get())

brightness= ttk.Scale(RHS,from_=0,to=100,orient=HORIZONTAL,command=brightness_changed,variable=brightness_value)
brightness.place(x=90,y=200)
brightness.set(sbc.get_brightness()[0])

#############################################
RHD = Frame(Body, width=470, height=190, bg="#fff", highlightbackground="gray")
RHD.place(x=330, y=255)

root.mainloop()
