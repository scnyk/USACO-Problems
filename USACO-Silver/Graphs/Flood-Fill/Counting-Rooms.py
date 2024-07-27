'''
This is a CSES Problem found at https://cses.fi/problemset/task/1192/

Flood Fill uses a simple Depth-First Search to identify connected components within a grid (any nxm input) and counts the

Counting Rooms follows the regular Flood Fill algo, searching for "rooms" (clusters of "." characters) in a given floor layout. 

'''

# retrieve stdin input and initialize the 2d list to store the grid
h,w = (int(i) for i in input().split())
grid = []
for _ in range(h):
    grid.append([i for i in input()])   
visited = set()

# initialize return variable
rooms = 0

# repeat dfs while cell is unvisited, within grid bounds, and is a floor cell (".")
def floodFill(i,j):
    if (i,j) in visited: return
    if i<0 or j<0 or i>=h or j>=w: return
    if grid[i][j] == ".":
        visited.add((i,j)) 
        floodFill(i+1,j)
        floodFill(i-1,j)
        floodFill(i,j+1)
        floodFill(i,j-1)

# call dfs at each unvisited floor cell
def countRooms():
    global rooms
    for i in range(h):
        for j in range(w):
            if grid[i][j]=="." and (i,j) not in visited:
                rooms+=1
                floodFill(i,j)

# execute and print the room count
countRooms()
print(rooms)
