####### ------------- Imports ---------------######
# Import tkinter module
import tkinter as tk
import tkinter.messagebox as tkMessageBox
from tkinter.filedialog import asksaveasfilename

# Import Matplotlib, math and statitics
import numpy as np  # To use array of numbers instead of list
import matplotlib.pyplot as plt # To plot graphics
from matplotlib.figure import Figure
import random # To generate random numbers
from statistics import mean # To use mean from statistics package
import math # To use log and pi methods.

# To import integration features (between tkinter and matplotlib)
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg # used to integrate tkinter and matplotlib
plt.style.use("ggplot")

# Imports not being used (here as reference)
#import tkinter.filedialog # To use dialogs (like open file, save file)
#import tkinter import filedialog as fd # Different way of calling it

### defs at the begin of the code ### defs are the functions ###
def graph(f,c):
    window_size_N = 5 # Set a initial value
    f.clear()
    # Now lets import .txt file
    # 3 Column, being packet number, RSSI Downlink, PSR (packet success rate)
    file = open("gerencia.txt", mode='r')
    #print(file.read())

    RSSIdl = np.loadtxt("gerencia.txt", delimiter=';', usecols=[1])
    #print(RSSIdl)     
    #file.close() #? I am considering that I have all the data already

    val_run = 0
    std_deviation_running = np.array(0)
    #print(type(std_deviation_running))
    # Shows how many dimention the array has, not elements
    # print(std_deviation_running.ndim) 
    # std_deviation_running = np.append(std_deviation_running, 10)
    
    #print(std_deviation_running)
    for val in RSSIdl:
        # val returns <class 'numpy.float64'>
        # To run over all the random values by incrementing 1
        val_run = val_run+1 
        # array_partial = initial value up to window size
        # then do it again, but initial value + 1 up to window size + 1
        array_partial = RSSIdl[val_run:window_size_N+val_run]
        # now, I need to add to an array, each value of std deviation
        #print(np.std(array_partial))
        std_deviation_running = np.append(std_deviation_running, np.std(array_partial))
        #print('Standard deviation: ' + str(np.float64(np.std(array_partial))))
        #print(array_partial)
    #print(std_deviation_running)
    #plt.figure(1)
    ax = f.add_subplot()
    ax.plot(std_deviation_running, label='Running statistics')     # plt.plot(std_deviation_running) 
    ax.set_xlabel('Time domain') # plt.xlabel('Time domain')
    ax.set_ylabel('Standard deviation') #plt.ylabel('Standard deviation')
    
    f.subplots_adjust(left=0.05, bottom=0.2, right=0.98, top=0.95, wspace=None, hspace=None)
    canvas.draw() # instead of plt.show()
    
    file.close()
    window.after(1000, graph,f,c) # Call function again after 1000 mili seconds.
    

def save_value():
    entry = window_size.get() # Takes string fist
    window_size_N = int(entry) # Then convert str to int
    print(window_size_N)
    if window_size_N <= 1:
        print('Window size cannont be lesser than 2')
    elif window_size_N > 101: #elif = else if
        print('Window size cannont be greater than 101')
    else:
        print('Running statistcs considering window size of: ', window_size_N)

def callback():
    if tkMessageBox.askokcancel("Sair", "Tem certeza que deseja sair?"):
        window.destroy()

def save(ff):
        ftypes = [('.png (PNG)', '*.png')]
        f = asksaveasfilename(filetypes=ftypes, defaultextension=".png")

        print(f)

        if f != '':
            ff.savefig(f)

''' this coments
more than just
one line '''
################################################### CODE ##############################################


#### ------------ Window Creation ---------------- ####
    
# Initialize the window manager
window = tk.Tk() # blank window with close, maximize, and minimize buttons on the top
# (Optional) Rename the GUI window
window.title("N6 Running Statistics")
# Geometry management 
window.geometry("1000x380")
window.resizable(0,0) # User can't resize window
# Let's create a frame
frame = tk.Frame(master = window, borderwidth=1, relief='sunken')
frame.place(x=10,y=10,width=980,height=360)


# Define the label widget
#label = tk.Label(window, text ="Hello World!").pack() # a widget that is used to insert some text into the window

#### -------------- Buttons ------------------- ####

# Create text to assist user 
text = tk.Label(frame, text = "Tamanho da janela:")
text.place(x=110,y=318)
# Create box to receive value
window_size = tk.Entry(frame, width=10)
window_size.place(x=230,y=319)
window_size.insert(5, "5")
# Create button to save value to the variable
b_save_value = tk.Button(frame,text="GRAVAR", width=10, command = save_value)
b_save_value.place(x=300, y=315)
b_save_value.config(state="normal")


fig = Figure(figsize=(9.8, 3), facecolor='white') 
# Figure: Area to plot the mathplot graph
# figsize=(x,y) in units, facecolor='white' to make background of the figure white
canvas = FigureCanvasTkAgg(fig, master = frame)
canvas.get_tk_widget().grid()
graph(fig,canvas)

b_save_image = tk.Button(frame, text='Salvar Gráfico', command=lambda:save(fig))
b_save_image.place(x=760,y=315)

#### -------------- Mainloop method ------------------ ####
window.protocol("WM_DELETE_WINDOW", callback)
window.mainloop() # method to display the window until you manually close it




