# weather_app.py
from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import messagebox, ttk 
from timezonefinder import TimezoneFinder  
from datetime import datetime
import requests
import pytz 

def run_weather_app():
    root = tk.Tk()
    root.title("Weather App")
    root.geometry("900x500+300+200")
    root.config(bg="white")
    root.resizable(False, False)
    
    #search box
    search_image = PhotoImage(file="./images/rect.png")
    search_label = Label(root, image=search_image, bg="white")
    search_label.place(x=50, y=50)

    textfield = Entry(root, justify="center" ,font=("Arial", 20), bg="white", border=0)   
    textfield.place(x=80, y=50)
    textfield.focus()

    search_icon = PhotoImage(file="./images/search.png")
    search_button = Button(root, image=search_icon, bg="white", border=0)
    search_button.place(x=330, y=50)
    root.mainloop()
