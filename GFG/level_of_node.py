# Find the level of given node in an Undirected Graph

# Given an undirected graph with V vertices and E edges and a node X, The task is to find the level of node X in the undirected graph. If X does not exist in the graph then return -1.

# Note: Traverse the graph starting from vertex 0.


def findLevel(N , edges, x):
    maxVertex = 0

    # Checking the MAX vertex!
    for it in edges:
        maxVertex = max(maxVertex, max(it[0], it[1]))

    # Creating adjacency list
    adj = [[] for j in range(maxVertex + 1)]

    for i in range(len(edges)):
        print("i :", i)
        adj[edges[i][0]].append(edges[i][1])
        adj[edges[i][1]].append(edges[i][0])

    if (X > maxVertex or len(adj[X]) == 0):
        return -1

    q = []
    q.append(0)
    level=0

    visited=[0]*(maxVertex+1)
    visited[0]=1

#     BFS Traversal

    while (len(q)>0):
        sz = len(q)
        while(sz > 0):
            currentNode = q[0]
            q.pop(0)
            if(currentNode==X):
                return level

            for it in adj[currentNode]:
                if (not visited[it]):
                    q.append(it)
                    visited[it]=1
                sz = sz-1
        level = level+1

    return -1



V = 5
Edges = [[0,1],[0,2],[1,3],[2,4]]
X = 10

level=findLevel(V,Edges,X)
print(level)