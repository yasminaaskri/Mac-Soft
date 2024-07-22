from tkinter import *
from tkinter import ttk
from tkinter import messagebox ,ttk
import tkinter as tk
import platform
import psutil

#colors 
bg_color = "#343434"


root=Tk()
root.title("System Information")
root.geometry("850x500+300+150")
root.resizable(False,False)
root.config(bg=bg_color)


#icon
icon=PhotoImage(file="./images/icon.png")
root.iconphoto(False,icon)

Body=Frame(root , width=900,height=600 ,bg="#d8e2dc")
Body.pack(pady=20,padx=20)
#---------------------------------PC INFO---------------------------------

LHS=Frame(Body , width=310,height=435 ,bg="#fff", highlightbackground="red" )
LHS.place(x=10,y=10)

#pc photo
photo=PhotoImage(file="./images/pc.png")
myimage=Label(LHS, image=photo )
myimage.place(x=2 , y=20)

mysystem=platform.uname()

l1=Label(LHS , text=mysystem.node , bg="#fff", font=('Acumin Variable Concept' ,15 , 'bold') , justify="center")
l1.place(x=10 , y=200)
l2=Label(LHS, text=f"Version:{mysystem.version}" ,bg="#fff" , font=('Acumin Variable Concept' ,8) , justify="center")
l2.place(x=10 , y=230)
l3=Label(LHS, text=f"System:{mysystem.system}" ,bg="#fff" , font=('Acumin Variable Concept' ,15) , justify="center")
l3.place(x=10 , y=260)
l4=Label(LHS, text=f"Machine:{mysystem.machine}" ,bg="#fff" , font=('Acumin Variable Concept' ,15) , justify="center")
l4.place(x=10 , y=290)
l5=Label(LHS, text=f"Total RAM installed :{round (psutil.virtual_memory().total/1000000000 , 2)} GB" ,bg="#fff" , font=('Acumin Variable Concept' ,15) , justify="center")
l5.place(x=10 , y=320)
l6=Label(LHS, text=f"Processor:{mysystem.processor}" ,bg="#fff" , font=('Acumin Variable Concept' ,7) , justify="center")
l6.place(x=10 , y=350)
#------------------------------

RHS=Frame(Body , width=470,height=230 ,bg="#fff", highlightbackground="red" )
RHS.place(x=330,y=10)

#-------------------------------


RHD=Frame(Body , width=470,height=190 ,bg="#fff", highlightbackground="red" )
RHD.place(x=330,y=255)

root.mainloop()
