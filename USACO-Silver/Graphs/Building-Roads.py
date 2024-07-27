'''
https://cses.fi/problemset/task/1666
'''

from collections import deque

# get vertex and edge count
n, e = [int(i) for i in input().split()]

# create and adjacency list to iterate along edges between vertices
adj = [[] for _ in  range(n+1)]
for edge in range(e):
    u,v = (int(i) for i in input().split())
    adj[u].append(v)
    adj[v].append(u)

# dfs using stack (using deque - can replace with list for worse time complexity)
cities = []
roads = -1

# create a set to track previously traversed vertices
visited = set()

# add all traversed vertices to visited set
def dfs(starter):
    stack = deque()
    stack.append((starter))
    while stack:
        i = stack.pop()
        visited.add(i)
        for connection in adj[i]:
            if connection not in visited:
                stack.append(connection)

# perform dfs at each index in node range
for node in range(1,n):
    if node not in visited:
        roads+=1
        cities.append(node)
        dfs(node)

# print road count, and city connecting points (if any)
print(roads)
if roads>=1:
    for i in range(0,roads):
        print(cities[i],cities[i+1])

    


