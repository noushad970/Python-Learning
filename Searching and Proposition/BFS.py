graphs={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F','G'],
    'D':[],
    'E':[],
    'F':[],
    'G':[]
}

visited=[]
queue=[]

def bfs(graphs,visited,queue,root):
    visited.append(root)
    queue.append(root)
    while queue:
        m=queue.pop(0)
        print(m," ")
        for ng in graphs[m]:
            if ng not in visited:
                visited.append(ng)
                queue.append(ng)
bfs(graphs,visited,queue,'A')