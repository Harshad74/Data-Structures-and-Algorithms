num_nodes=5
edges=[(0,1),(0,4),(1,2),(1,3),(1,4),(2,3),(3,4)]

class Graph:
    def __init__(self,num_nodes,edges):
        self.num_nodes=num_nodes
        self.data=[[] for _ in range(num_nodes)]
        for n1,n2 in edges:
            self.data[n1].append(n2)
            self.data[n2].append(n1)

graph1=Graph(num_nodes,edges)
print(graph1.data)


def bfs(graph,root):
    queue=[]
    discovered=[False]*len(graph.data)
    distance=[None]*len(graph.data)
    parent=[None]*len(graph.data)

    discovered[root]=True
    queue.append(root)
    distance[root]=0
    idx=0

    while(idx<len(queue)):

        current=queue[idx]
        idx+=1

        for node in graph.data[current]:
            if not discovered[node]:
                distance[node]=1+distance[current]
                parent[node]=current
                discovered[node]=True
                queue.append(node)

    return queue,distance,parent  

print(bfs(graph1,3))



def dfs(graph,root):
    stack=[]
    discovered=[False]*len(graph.data)
    result=[]

    stack.append(root)
    while len(stack)>0:
        current=stack.pop()
        if not discovered[current]:
            discovered[current]=True
            result.append(current)
            for node in graph.data[current]:
                if not discovered[node]:
                    stack.append(node)

    return result

print(dfs(graph1,3))

