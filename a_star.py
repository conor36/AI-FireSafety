import time as t


#each colour has its own representation white = path, black = wall, orange = fire, red = path taken
colour = {7:"green", 6:"orange", 5:"red", 4: "red", 3: "green", 2: "pink", 1: "#3d3e3f", 0: "#e0eefc"}

# redraws the entire canvas based on the above colour
def draw_canvas(canvas, plan, col_len, row_len, event=None):
    for i in range(0, col_len):
        for j in range(0, row_len):
            canvas.create_rectangle(j * 32, i*32, (j+1) * 32, (i + 1) * 32, fill=colour[plan[i][j].wall])
            #rectangles are 16 pixels in width and height
    canvas.pack()


#function to get the next available pos to be explored
def find_pos(inherit, plan, col_len, row_len):

    add_list = [1, 0, -1, 0, 1]
    ret_list = []
    for i in range(4):
        x = add_list[i] + inherit.x
        y = add_list[i+1] + inherit.y
        # stops execution at first false so out of bounds error is not thrown
        if x in range(0,row_len) and y in range(0,col_len) and plan[y][x].wall != 1 and plan[y][x].wall != 6 and plan[y][x].check_g(inherit):
            plan[y][x].inherit = inherit
            plan[y][x].g = inherit.g + 1
            plan[y][x].set_f()              
            #sets f and g values for search
            ret_list.append(plan[y][x])
    return ret_list


#function draws visited pos and returns optimum path, returns errors if path imposible/out of range
def a_star(canvas, plan, start_pos, exit_pos, col_len, row_len, root):
    draw_canvas(canvas, plan, col_len, row_len)

    for i in range(0, col_len):
        for j in range(0, row_len):
            #sets manhattan distance for each pos
            plan[i][j].set_manhattan(exit_pos)

    start_pos.g = 0

    open_list = find_pos(start_pos, plan, col_len, row_len)
    closed_list = [start_pos]

    visited = False 
    
    while open_list and not visited:
        # sort based on f value
        open_list.sort(key=lambda pos: pos.f)

        next_pos = open_list.pop(0)

        if next_pos == exit_pos:
            visited = True
        else:
            next_pos.wall = 2  # this pos has been visited
            closed_list.append(next_pos) # append to closed list
            add_list = [x for x in find_pos(next_pos, plan, col_len, row_len) if x not in closed_list]
            open_list.extend(add_list)

        canvas.delete("all") 
        draw_canvas(canvas, plan, col_len, row_len)
        root.update() # updates and draws on top of canvas
        #t.sleep(speed)

    if not visited:
        canvas.create_text((row_len*8),(col_len*8),text="Exit cannot be reached",fill="red",font="Helvetica 40 bold")
        canvas.pack()
        return

    else: # optimum exit found and displays
        curr_pos = exit_pos.inherit
        while start_pos != curr_pos:
            curr_pos.wall = 4
            canvas.delete("all") # deletes saved information, speeds up program
            draw_canvas(canvas, plan, col_len, row_len)
            root.update() # updates and draws on top of canvas
            #t.sleep(speed)
            curr_pos = curr_pos.inherit
    return
