import sys

def prim_mst(graph, start_node):
    num_vertices = len(graph)
    key = [sys.maxsize] * num_vertices
    parent = [-1] * num_vertices
    mst_set = [False] * num_vertices

    key[start_node] = 0

    for _ in range(num_vertices - 1):
        u = min_key(key, mst_set)
        mst_set[u] = True

        for v in range(num_vertices):
            if graph[u][v] != 0 and  mst_set[v]==False and graph[u][v] < key[v]:
                parent[v] = u
                key[v] = graph[u][v]

    print_mst(parent, graph)

def min_key(key, mst_set):
    min_val = sys.maxsize
    min_index = -1

    for v in range(len(key)):
        if  mst_set[v]==False and key[v] < min_val:
            min_val = key[v]
            min_index = v

    return min_index

def print_mst(parent, graph):
    print("Edge \tWeight")
    for i in range(1, len(parent)):
        print(parent[i], "-", i, "\t", graph[i][parent[i]])

# Example Usage
graph = [
    [0, 5, 9, 2],
    [0, 5, 9, 3],
    [9,0, 0, 8],
    [2, 3, 8, 0],

]
start_node = 0
prim_mst(graph, start_node)

