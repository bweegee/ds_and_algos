# https://www.hackerrank.com/challenges/bfsshortreach/problem?isFullScreen=true
from collections import defaultdict

def get_graph(edges):
    graph = defaultdict(set)
    for edge in edges:
        graph[edge[0]].add(edge[1])
        graph[edge[1]].add(edge[0])
    return graph
    
def bfs(n, m, edges, s):
    # Write your code here
    graph = get_graph(edges)
    queue = [s]
    distances = [-1] * (n + 1)
    distances[s] = 0
    
    while queue:
        node = queue.pop(0)
        for neighbor in graph[node]:
            if distances[neighbor] == -1:
                distances[neighbor] = distances[node] + 6
                queue.append(neighbor)
                
    #pop start node and 0 index
    distances.pop(s)
    distances.pop(0)
    return distances[:n+1]
