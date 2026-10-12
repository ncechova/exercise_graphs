def build_adjacency_list(edges, directed=False):
    adjacency_list = {}
    for edge in edges:
        i, j = edge
        if i not in adjacency_list:
            adjacency_list[i] = []
        if j not in adjacency_list:
            adjacency_list[j] = []
        adjacency_list[i].append(j)
        if not directed:
            adjacency_list[j].append(i)
    return adjacency_list


def degrees(graph):
    return {vertex: len(neighbors) for vertex, neighbors in graph.items()}


def in_out_degree(graph):
    in_degree = {vertex: 0 for vertex in graph}
    out_degree = {vertex: len(neighbors) for vertex, neighbors in graph.items()}
    for neighbors in graph.values():
        for neighbor in neighbors:
            if neighbor not in in_degree:
                in_degree[neighbor] = 0
            in_degree[neighbor] += 1
    return in_degree, out_degree


# task 3
def dfs(graph, start):
    if start not in graph:
        return []

    visited = []
    seen = set()
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex in seen:
            continue
        seen.add(vertex)
        visited.append(vertex)
        for neighbor in sorted(graph.get(vertex, []), reverse=True):
            if neighbor not in seen:
                stack.append(neighbor)
    return visited


def connected_components(graph):
    components = []
    seen = set()
    for vertex in sorted(graph):
        if vertex in seen:
            continue
        component = set(dfs(graph, vertex))
        components.append(component)
        seen |= component
    return components


def is_weakly_connected(graph):
    if not graph:
        return True

    shadow = {vertex: [] for vertex in graph}
    for u, neighbors in graph.items():
        for v in neighbors:
            if v not in shadow:
                shadow[v] = []
            if v not in shadow[u]:
                shadow[u].append(v)
            if u not in shadow[v]:
                shadow[v].append(u)
    return len(connected_components(shadow)) == 1


# task 4
def eulerian_type(graph, directed=False):
    if not graph:
        return "circuit"

    if not directed:
        if len(connected_components(graph)) != 1:
            return "none"
        odd = sum(degree % 2 for degree in degrees(graph).values())
        if odd == 0:
            return "circuit"
        if odd == 2:
            return "path"
        return "none"

    if not is_weakly_connected(graph):
        return "none"

    in_degree, out_degree = in_out_degree(graph)
    starts = 0
    ends = 0
    for vertex in graph:
        excess = out_degree[vertex] - in_degree[vertex]
        if excess == 1:
            starts += 1
        elif excess == -1:
            ends += 1
        elif excess != 0:
            return "none"

    if starts == 0 and ends == 0:
        return "circuit"
    if starts == 1 and ends == 1:
        return "path"
    return "none"

#task 1
def task1(adjacency_list_undirected, adjacency_list_directed):
    print(f"Adjacency List (Undirected): \n{adjacency_list_undirected}")
    print(f"Adjacency List (Directed): \n{adjacency_list_directed}")
    print(f"Degrees (Undirected): \n{degrees(adjacency_list_undirected)}")
    print(f"In/Out Degrees (Directed): \n{in_out_degree(adjacency_list_directed)}")
    return 

# task 3
def task3(adjacency_list_undirected, adjacency_list_directed, start_vertex='P2'):
    print(f"DFS (Undirected) starting from {start_vertex}: {dfs(adjacency_list_undirected, start_vertex)}")
    print(f"DFS (Directed) starting from {start_vertex}: {dfs(adjacency_list_directed, start_vertex)}")    
    print(f"Connected Components (Undirected): {connected_components(adjacency_list_undirected)}")
    print(f"Connected Components (Directed): {connected_components(adjacency_list_directed)}")
    print(f"Is Weakly Connected (Directed): {is_weakly_connected(adjacency_list_directed)}")
    return   
# task 4
def task4():
    G1 = [('A', 'D'), ('A', 'I'), ('B', 'D'), ('B', 'F'), ('B', 'G'), ('C', 'E'), ('C', 'H'), ('C', 'J'), ('C', 'K'), ('D', 'F'), ('D', 'G'), ('E', 'J'), ('H', 'J'), ('J', 'K')]
    G3 = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A'), ('D', 'E'), ('E', 'F'), ('F', 'G'), ('G', 'D')]
    G4 = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A'), ('D', 'E'), ('E', 'F'), ('G', 'D')]
    G5a = [(1, 2), (2, 3), (3, 1), (1, 4), (4, 1)]
    G5b = [(1, 2), (2, 3), (3, 1), (1, 4)]
    Konigsberg =  [('A', 'B'), ('A', 'B'), ('A', 'C'), ('A', 'C'), ('A', 'D'), ('B', 'D'), ('C', 'D')]
    print(f"Eulerian type of G1: {eulerian_type(build_adjacency_list(G1))}")
    print(f"Eulerian type of G3: {eulerian_type(build_adjacency_list(G3))}")
    print(f"Eulerian type of G4: {eulerian_type(build_adjacency_list(G4))}")
    print(f"Eulerian type of G5a: {eulerian_type(build_adjacency_list(G5a, directed=True), directed=True)}")
    print(f"Eulerian type of G5b: {eulerian_type(build_adjacency_list(G5b, directed=True), directed=True)}")
    print(f"Eulerian type of Konigsberg: {eulerian_type(build_adjacency_list(Konigsberg))}")
    return

if __name__ == "__main__":
    V = {'P1', 'P2', 'P3', 'P4', 'P5'}
    E = [('P1', 'P2'), ('P1', 'P3'), ('P2', 'P3'), ('P3', 'P4'), ('P4', 'P5')]

    V1 = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'}   
    E1 = [('A', 'D'), ('A', 'I'), ('B', 'D'), ('B', 'F'), ('B', 'G'), ('C', 'E'), ('C', 'H'), ('C', 'J'), ('C', 'K'), ('D', 'F'), ('D', 'G'), ('E', 'J'), ('H', 'J'), ('J', 'K')]

    adjacency_list_undirected = build_adjacency_list(E)
    adjacency_list_directed = build_adjacency_list(E, directed=True)
    adjacency_list_undirected1 = build_adjacency_list(E1)
    adjacency_list_directed1 = build_adjacency_list(E1, directed=True)
    # task1(adjacency_list_undirected1, adjacency_list_directed1)
    # task3(adjacency_list_undirected1, adjacency_list_directed1, start_vertex='A')
    task4()