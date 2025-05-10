#dfs 
# to implement dfs traversal, goal search(any path, best path), depth limited dfs, and iterative deepening dfs

graph={
'A':['B','C'],
'B':['D','E'],
'C':['F','G'],
'D':[],
'E':[],
'F':[],
'G':[],
}

start=input("enter start node:").strip().upper()

def dfs_traversal(graph):
 closed=[]
 open=[start]
 while open:
   node=open.pop()
   if node not in closed:
     closed.append(node)
     neighbours=graph[node]
   for i in neighbours:
     open.append(i)
 return closed
print("\nDFS Traversal is:",dfs_traversal(graph))