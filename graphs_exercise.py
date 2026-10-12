V = {'P1', 'P2', 'P3', 'P4', 'P5'}
E = [('P1', 'P2'), ('P1', 'P3'), ('P2', 'P3'), ('P3', 'P4'), ('P4', 'P5')]

V1 = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'}   
E1 = [('A', 'D'), ('A', 'I'), ('B', 'D'), ('B', 'F'), ('B', 'G'), ('C', 'E'), ('C', 'H'), ('C', 'J'), ('C', 'K'), ('D', 'F'), ('D', 'G'), ('E', 'J'), ('H', 'J'), ('J', 'K')]


def build_adjacency_list(edges, directed=False):
    adjacency_list = {}
    for edge in edges:
        i,j = edge
        if i not in adjacency_list:
            adjacency_list[i] = []
        if j not in adjacency_list:
            adjacency_list[j] = []
        adjacency_list[i].append(j)
        if not directed:
            adjacency_list[j].append(i)
    return adjacency_list

def degrees(graph):
    degrees_dict = {vertex: 0 for vertex in graph}
    for vertex, neighbors in graph.items():
        degrees_dict[vertex] = len(neighbors)
        for neighbor in neighbors:
            if neighbor not in degrees_dict:
                degrees_dict[neighbor] = 0
    return degrees_dict

def in_out_degree(graph):
    in_degree = {vertex: 0 for vertex in graph}
    out_degree = degrees(graph)
    for vertex, neighbors in graph.items():
        for neighbor in neighbors:
            if neighbor not in in_degree:
                in_degree[neighbor] = 0
            in_degree[neighbor] += 1
    return in_degree, out_degree
#task 1
def task1():
    print(f"Adjacency List (Undirected): \n{adjacency_list_undirected}")
    print(f"Adjacency List (Directed): \n{adjacency_list_directed}")
    print(f"Degrees (Undirected): \n{degrees(adjacency_list_undirected)}")
    print(f"In/Out Degrees (Directed): \n{in_out_degree(adjacency_list_directed)}")
    return 

# task 3
def dfs(graph, start):
    visited = []          # visit order
    seen = set()
    stack = [start]
    while stack:
        # print(f"Stack: {stack}")
        vertex = stack.pop()
        # print(f"Visiting: {vertex}")
        if vertex in seen:
            continue
        seen.add(vertex)
        visited.append(vertex)
        # print(f"neighbors of {vertex}: {graph.get(vertex, [])}")
        for neighbor in sorted(graph.get(vertex, []) , reverse=True):
            if neighbor not in seen:
                stack.append(neighbor)
    return visited

def connected_components(graph):
    components = []
    seen = set()
    for vertex in sorted(graph):
        if vertex not in seen:
            component = set(dfs(graph, vertex))
            components.append(component)
            seen |= component
    return components

def is_weakly_connected(graph):
    shadow = {vertex: [] for vertex in graph}
    for u, neighbors in graph.items():
        for v in neighbors:
            shadow[u].append(v)
            shadow[v].append(u)
    return len(connected_components(shadow)) == 1


def task3(adjacency_list_undirected, adjacency_list_directed, start_vertex='P2'):
    print(f"DFS (Undirected) starting from {start_vertex}: {dfs(adjacency_list_undirected, start_vertex)}")
    print(f"DFS (Directed) starting from {start_vertex}: {dfs(adjacency_list_directed, start_vertex)}")    
    print(f"Connected Components (Undirected): {connected_components(adjacency_list_undirected)}")
    print(f"Connected Components (Directed): {connected_components(adjacency_list_directed)}")
    print(f"Is Weakly Connected (Directed): {is_weakly_connected(adjacency_list_directed)}")
    return   

if __name__ == "__main__":
    adjacency_list_undirected = build_adjacency_list(E)
    adjacency_list_directed = build_adjacency_list(E, directed=True)
    adjacency_list_undirected1 = build_adjacency_list(E1)
    adjacency_list_directed1 = build_adjacency_list(E1, directed=True)
    # task1()
    task3(adjacency_list_undirected1, adjacency_list_directed1, start_vertex='A')