import tkinter as tk
from tkinter import *
from a_star import *
from node import *
from search import *
from fire import *
from smoke import *
val = 10
speed = 0



def main():
    with open("plan.txt") as text:
        # strips the new line characters off the the plan
        plan = [list(line.strip()) for line in text]
        
    # returns col and row lens
    col_row_len = init_validate(plan)

    # row/col len list empty, invalid plan
    if not col_row_len:
        print("There was an error with the layout of the plan")
        exit(0)

    col_len = col_row_len[0]
    row_len = col_row_len[1]
    
    for i in range(0,col_len):
        for j in range(0,row_len):
            # pos.py class
            plan[i][j] = pos(int(plan[i][j]), j, i)
            
    entrance_pos = find_entrance(plan, col_len, row_len)
    exit_pos = find_exit(plan, col_len, row_len)
    fire_pos = find_fire(plan, col_len, row_len)



    if entrance_pos is None or exit_pos is None:
        print("There is an error with either the entrance or the exit")
        exit(0)
    # initial frame
    root = Tk()
    canvas = Canvas(root, width=(32*row_len), height=(32*col_len))
    #canvas = Rectangle(root, width=(35*row_len), height=(35*col_len))
   

    

    #canvas.create_line(15, 25, 200, 25)
    #canvas.create_text(500,150,font = "Time 50 italic bold", text="Welcome")   
    #canvas.pack(fill=BOTH, expand=1)

    def valu(v1):
        global val
        
        val = v1
          

    
    w = Scale(root, from_=0, to=200, orient=HORIZONTAL, label="minutes", command=valu)
        
    canvas=Canvas(root, width=(32*row_len), height=(32*col_len))
    canvas.pack()
    w.pack()
    
    def draw_canvas(canvas, plan, col_len, row_len, event=None):
        for i in range(0, col_len):
            for j in range(0, row_len):
                canvas.create_rectangle(j * 32, i*32, (j+1) * 32, (i + 1) * 32, fill=colour[plan[i][j].wall])
                #rectangles are 16 pixels in width and height
        canvas.pack()

    draw_canvas(canvas, plan, col_len, row_len)

    #w = Scale(root, from_=0, to=200, orient=HORIZONTAL, command=valu)

    #w.pack()
       
    root.title("A-Star Demonstration")

    #a_star(canvas, plan, entrance_pos, exit_pos, col_len, row_len, root)

   # def valu(val):

    #    print(val)
    '''

        if val <= 20:
            val = val * 0
        
        if val > 20 and val <= 60: 
            val = val / 4
        
        if val > 61 and val <=119:
            val = val / 3
        
        if val > 120 and val <=1000:
            val = val / 2 
        print(val)
    '''

    def mainy():
        global val
        print(val, "mainly")
        fire_main(canvas, plan, fire_pos, col_len, row_len, val, root) 
        a_star(canvas, plan, entrance_pos, exit_pos, col_len, row_len, root)
    
    button = tk.Button(root, 
        text="GO", 
        fg="red",
        command=mainy)
    button.pack(side=tk.TOP)
    
    '''
    def mainy(fire_main, a_star):

        fire_main(canvas, plan, fire_pos, col_len, row_len, root) 
        a_star(canvas, plan, entrance_pos, exit_pos, col_len, row_len, root)
    #fire_main(canvas, plan, fire_pos, col_len, row_len, root)        #smoke_main(canvas, plan, fire_pos, col_len, row_len, root)
    '''
    # frame main loop after functionality
    root.mainloop()



if __name__ == '__main__':
    main()