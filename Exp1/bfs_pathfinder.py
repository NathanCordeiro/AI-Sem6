# To implemment BFS traversal and goal search

graph={
'A':['B','C'],'B':['D','E'],'C':['F','G'],'D':[],'E':[],'F':[],'G':[],
      }
start=input("enter start node:").strip().upper()

def bfs_traversal(graph):
    closed=[]
    open=[start]
    while open:
      node=open.pop(0)
      if node not in closed:
        closed.append(node)
        neighbours=graph[node]
        for i in neighbours:
          open.append(i)
    return closed
   
print("\nBFS traversal is: ",bfs_traversal(graph))