from GraphClass import Graph, Tree


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

'''
G = string_to_graph(file_contents)
G.add_edge((1, 2))
G.neighbor_matrix()
'''


T = Tree(20)
tree_edges = [
    (1,2),(1,3),(1,4),(2,5),(2,6),(2,7),(2,8),(6,14),(6,15),(6,16),(8,17),(3,9),(3,10),(4,11),(4,12),(4,13),(11,18),(13,19),(13,20)
]
for i in tree_edges:
    T.add_edge(i)

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

print(T.neighbors)
print(T.create_code(1))

T2 = tree_from_code("0001001010110100111001011000110100101111")
print(T2.create_code(11))