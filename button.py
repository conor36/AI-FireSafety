import tkinter as tk
from tkinter import *
root=tk.Tk()

#creates white canvas
c = tk.Canvas(root, height=900, width=1200, bg='white')
c.pack()
img = PhotoImage(file='/Users/conorreilly/Desktop/plan2.png')
root.wm_attributes('-alpha', 0.7) 
c.create_image(300, 600, image=img)
c.pack()


cell_size = (30,30)

def create_grid(event=None):
    w = c.winfo_width() # Get current width of canvas
    h = c.winfo_height() # Get current height of canvas
    #c.delete('grid_line') # Will only remove the grid_line

    # Creates all vertical lines at intevals of 100
    for i in range(0, w, cell_size[0]):
        c.create_line([(i, 0), (i, h-1)], tag='grid_line')

    # Creates all horizontal lines at intevals of 30
    for i in range(0, h, cell_size[1]):
        c.create_line([(0, i), (w-1, i)], tag='grid_line')



    
    

"""
def target(event):
    target_cell = (event.x // cell_size[0], event.y // cell_size[1])
    #print(target_cell)
root.bind("<Button-1>", target)
"""
def start(event):
    start_cell = (event.x // cell_size[0], event.y // cell_size[1])
    print(start_cell)
    #print(event.x//cell_size[0])
    #w = c.winfo_width()
    #h =c.winfo_height()
    c.create_rectangle([(((event.x//30)*30),((event.y//30)*30),(event.x//30)*30+30),((event.y//30)*30+30)], fill='blue')

    #for i in range(0, 300):
     #   c.create_line([(event.x, i),(event.y, i)], fill='green')





    


'''
def fill(event, create_grid): 

    s = tk.Canvas(root, height=30, width=30, bg='blue')
    s.pack(expand=False)
'''
    
root.bind("<Button-1>", start) 

c.bind('<Configure>', create_grid)

"""
def clicked(event):
    print("The user clicked at coordinates", event.x, event.y)
root.bind("<Button-1>", clicked)
"""

root.mainloop()