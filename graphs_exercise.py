#task 1
def task1():
    V = {'P1', 'P2', 'P3', 'P4', 'P5'}
    E = [('P1', 'P2'), ('P1', 'P3'), ('P2', 'P3'), ('P3', 'P4'), ('P4', 'P5')]

    def build_adjacency_list(edges, directed=False):
        adjacency_list = {}
        for edge in edges:
            i,j = edge
            if i not in adjacency_list:
                adjacency_list[i] = []
            adjacency_list[i].append(j)
            if not directed:
                if j not in adjacency_list:
                    adjacency_list[j] = []
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
    adjacency_list_undirected = build_adjacency_list(E)
    adjacency_list_directed = build_adjacency_list(E, directed=True)
    print(f"Adjacency List (Undirected): \n{adjacency_list_undirected}")
    print(f"Adjacency List (Directed): \n{adjacency_list_directed}")
    print(f"Degrees (Undirected): \n{degrees(adjacency_list_undirected)}")
    print(f"In/Out Degrees (Directed): \n{in_out_degree(adjacency_list_directed)}")
    return 

if __name__ == "__main__":
    task1()