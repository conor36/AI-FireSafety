import tkinter as tk
from tkinter import *
from a_star import *
from node import *
from search import *
from fire import *
from smoke import *

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
    canvas = Canvas(root, width=(32*row_len), height=(35*col_len))
    canvas.create_text((row_len*8),(col_len*8),text="Exit cannot be reached",fill="red",font="Helvetica 40 bold")
    canvas.update()
    canvas.pack()

    master = Tk()
    #canvas.create_line(15, 25, 200, 25)
    #canvas.create_text(500,150,font = "Time 50 italic bold", text="Welcome")   
    #canvas.pack(fill=BOTH, expand=1)
    w = Scale(master, from_=0, to=200, orient=HORIZONTAL)
    w.pack()
    
    root.title("A-Star Demonstration")

    #a_star(canvas, plan, entrance_pos, exit_pos, col_len, row_len, root)

    fire_main(canvas, plan, fire_pos, col_len, row_len, root) 
    #smoke_main(canvas, plan, fire_pos, col_len, row_len, root)
    #fire_main(canvas, plan, fire_pos, col_len, row_len, root)
    a_star(canvas, plan, entrance_pos, exit_pos, col_len, row_len, root)
    #fire_main(canvas, plan, fire_pos, col_len, row_len, root)


    # frame main loop after functionality
    root.mainloop()


if __name__ == '__main__':
    main()