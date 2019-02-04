# this file contains functions that perform


def init_validate(maze):
    column_len = len(maze)
    row_len = len(maze[0])
    # making sure all rows are equal length and everything in the rows is a 1 or a 0
    if all(len(rows) == row_len and all(items in ['0','1','5','6','7'] for items in rows) for rows in maze):
        return [column_len, row_len]
    else:
        return []



def find_entrance(maze, column_len, row_len):
    # entrance can only be in the last row
    
    #for i in maze[0]:
     #   if i.wall == 0:
      #      return i
    
    for i in range(0, column_len - 1):
        for j in range(0,row_len -1):
            if maze[i][j].wall == 5:
                return maze[i][j]
    
    return None




def find_exit(maze, column_len, row_len):
    # top check for exit
    for j in maze[0]:
        if j.wall == 0:
            return j

    # wall check, exit cannot be at the bottom
    for i in range(1, column_len - 1):
        for j in range(0,row_len -1):
            if maze[i][j].wall == 7:
                return maze[i][j]

    return None

def find_fire(maze, column_len, row_len):
    # entrance can only be in the last row
    
    #for i in maze[0]:
     #   if i.wall == 0:
      #      return i
    
    for i in range(2, column_len - 1):
        for j in [3,(row_len -1)]:
            if maze[i][j].wall == 6:

                return maze[-i][-j]
    
    return None

