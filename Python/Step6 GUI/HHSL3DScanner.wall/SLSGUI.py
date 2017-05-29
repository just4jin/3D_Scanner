import Tkinter as tk
import tkFileDialog
import numpy as np
import math
import cv2
import os
import glob
global captdirect
def pcapture():
    textvalcap= e.get()
    execfile("SL3DS1.projcapt.py")
def Procimg():
    execfile("SL3DS2.procimages.py")
def thresho():
    execfile("SL3DS3.adjustthresh.py")
def calcxy1xy2():
    execfile("SL3DS4.calcpxpy.py")
def calxyz():
    execfile("SL3DS5.calcxyz.py")
    execfile("SL3DS6.showpc.py")

root = tk.Tk()
root.title("3D scanning")

frame = tk.Frame(root)
frame.grid()
e = tk.Entry(root, width=60)
e.grid()
e.insert(0, "Enter capture directory name")
global textvalcap
global captdirect
photo1 = tk.PhotoImage(file="3dscan.gif")
photo2 = tk.PhotoImage(file="process.gif")
photo3 = tk.PhotoImage(file="threshold.gif")
photo4 = tk.PhotoImage(file="stereomatch.gif")
photo5 = tk.PhotoImage(file="pointcloud.gif")
photo6 = tk.PhotoImage(file="quitscan.gif")
textvalcap= e.get()
lbl=tk.Label(frame, text="HH Structured Light 3D Scanner")
lbl.grid()
pcapture = tk.Button(frame,  compound=tk.TOP, width=300, height=300, image=photo1 ,command=pcapture)
pcapture.grid(row=0, column=0)
Procimg = tk.Button(frame, text="Procimg", width=300, height=300, image=photo2 ,command=Procimg)
Procimg.grid(row=0, column=1)
thresho = tk.Button(frame, text="Threshold", width=300, height=300, image=photo3 ,command=thresho)
thresho.grid(row=0, column=2)
calcxy1xy2 = tk.Button(frame, text="calcxy1xy2", width=300, height=300, image=photo4 ,command=calcxy1xy2)
calcxy1xy2.grid(row=1, column=0)
calxyz = tk.Button(frame, text="calxyz", width=300, height=300, image=photo5 ,command=calxyz)
calxyz.grid(row=1, column=1)
button = tk.Button(frame, text="QUIT",  width=300, height=300, image=photo6, command=frame.quit)
button.grid(row=1, column=2)

root.mainloop()
root.destroy() # optional; see description below
