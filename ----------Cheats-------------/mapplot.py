import tkinter as tk 
import numpy as np
import matplotlib.pyplot as plt 
root = tk.Tk()
def fn():
	v1 = c1.get() v2 = c2.get()
	if v1==1 and v2==0:
		x = np.arange(-2*np.pi,2*np.pi,0.1) 
		y = np.sin(x)
		plotting(x,y,y,'Sine') 
	elif v2==1 and v1==0:
		x = np.arange(-2*np.pi,2*np.pi,0.1)
