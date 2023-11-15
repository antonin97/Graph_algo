from GraphClass import Graph, Tree
import copy


# parse string to Graph func
def string_to_graph(x):
    x = [[int(j) for j in i.split(" ")] for i in x.split("\n")]
    G = Graph(x[0][0])
    for edge in x[1:]:
        G.add_edge(edge)
    return G

# Open the file for reading
with open('test_graph.txt', 'r') as file:
    file_contents = file.read()


def check_valid_code(code):
    counter = 0
    for i in code:
        if i == "0":
            counter += 1
        else:
            if counter == 0:
                return False
            counter -= 1
    return counter == 0


def tree_from_code(code):
    if check_valid_code(code):
        edges = []
        vertex_counter = 2
        edge_stack = [1]
        for symbol in code[1:-1]:
            if symbol == "0":
                edges.append((edge_stack[-1], vertex_counter))
                edge_stack.append(vertex_counter)
                vertex_counter += 1
            else:
                edge_stack.pop()
        T = Tree(vertex_counter - 1)
        for edge in edges:
            T.add_edge(edge)
        return T
    else:
        print("Code invalid!")



def DFS(graph):
    number_of_components = 0
    vertices_visited = [False for i in range(graph.vertices)]

    def visit(vertex):
        print(f"Visited {vertex}")

        vertices_visited[vertex - 1] = True
        neighbors = sorted(graph.neighbors[vertex])
        for neighbor in neighbors:
            if not vertices_visited[neighbor - 1]:
                visit(neighbor)
        else:
            return

    for vertex in range(1, graph.vertices + 1):
        if vertices_visited[vertex - 1]:
            pass
        else:
            number_of_components += 1
            visit(vertex)


def BFS(graph, first=1, last=10):
    vertices_visited = [False for i in range(graph.vertices)]
    Q = [first]
    shortest_pres = [None for i in range(graph.vertices)]
    shortest_pres[first - 1] = 0

    while Q:
        current = Q[0]
        vertices_visited[current - 1] = True
        neighbors = sorted([i for i in graph.neighbors[current] if (i not in Q) and (not vertices_visited[i - 1])])
        for neigh in neighbors:
            shortest_pres[neigh - 1] = current
        Q = Q[1:] + neighbors
    way = []
    while last > 0:
        way = [last] + way
        last = shortest_pres[last - 1]
        if last == None:
            return []
    return way

def print_maze(maze):
    for i in maze:
        print("".join(i))

def maze_to_graph(maze):
    maze = [[j for j in i] for i in maze.split("\n")]
    vertice_counter = 1
    entrance = None
    exits = []
    treasure = None

    graph_array = []

    for row in maze:
        graph_row = []
        for element in row:
            if element == "X":
                graph_row.append(0)
            else:
                if element == "E":
                    entrance = vertice_counter
                    exits.append(vertice_counter)
                elif element == "e":
                    exits.append(vertice_counter)
                elif element == "T":
                    treasure = vertice_counter
                graph_row.append(vertice_counter)
                vertice_counter += 1
        graph_array.append(graph_row)
    
    G = Graph(vertice_counter - 1)
    
    for i in range(len(graph_array)):
        for j in range(len(graph_array[i])):
            if graph_array[i][j] == 0:
                continue
            vertex_current = graph_array[i][j]
            for k in range(-1, 2):
                for k in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                    if (i + k[0] < 0) or (j + k[1] < 0):
                        continue
                    try:
                        vertex_neighbour = graph_array[i + k[0]][j + k[1]]
                        G.add_edge((vertex_current, vertex_neighbour))
                    except IndexError:
                        pass
    way_to_treasure = BFS(G, entrance, treasure)
    maze_in = copy.deepcopy(maze)
    for i in range(len(graph_array)):
        for j in range(len(graph_array[i])):
            if graph_array[i][j] in way_to_treasure and maze_in[i][j] == "_":
                maze_in[i][j] = "."
    print("Way in")
    print("_" * 50)
    print_maze(maze_in)
    print("_" * 50)

    min_way_out = None
    
    for exit in exits:
        way = BFS(G, treasure, exit)
        if not way:
            continue
        if not min_way_out:
            min_way_out = way
        else:
            if len(way) < len(min_way_out):
                min_way_out = way
    
    maze_out = copy.deepcopy(maze)
    for i in range(len(graph_array)):
        for j in range(len(graph_array[i])):
            if graph_array[i][j] in min_way_out and maze_out[i][j] == "_":
                maze_out[i][j] = "."

    print("Way out")
    print("_" * 50)
    print_maze(maze_out)
    print("_" * 50)









''''

G1 = string_to_graph(file_contents)
G1.neighbor_matrix()

T1 = Tree(20)
tree_edges = [
    (1,2),(1,3),(1,4),(2,5),(2,6),(2,7),(2,8),(6,14),(6,15),(6,16),(8,17),(3,9),(3,10),(4,11),(4,12),(4,13),(11,18),(13,19),(13,20)
]
for i in tree_edges:
    T1.add_edge(i)


print(T1.create_code(1))

T2 = tree_from_code("0001001010110100111001011000110100101111")
print(T2)


G2 = Graph(10)
graph_edges = [
    (1,3),(1,2),(1,4),(2,5),(2,6),(3,6),(3,8),(3,4),(4,8),(4,9),(5,7),(7,8),(7,10),(8,9),(8,10),(9,10)
] 
for i in graph_edges:
    G2.add_edge(i)

BFS(G2, 4)
'''

# Open the file for reading
with open('maze.txt', 'r') as file:
    maze = file.read()
maze_to_graph(maze)

