class Graph:
    def __init__(self, vertices, edges=None):
        self.vertices = vertices
        if edges == None:
            self.edges = []
        else:   
            self.edges = edges
        self.neighbors = {i + 1:[] for i in range(vertices)}

    def __repr__(self):
        return str(self.neighbors)

    def add_edge(self, edge):
        if edge[0] == edge[1]:
            pass
        # valid edge
        elif (isinstance(edge[0], int) and 1 <= edge[0] <= self.vertices) and (isinstance(edge[1], int) and 1 <= edge[1] <= self.vertices):
            if (edge[0], edge[1]) in self.edges or (edge[1], edge[0]) in self.edges:
                pass
            self.edges.append((edge[0], edge[1]))
            self.neighbors[edge[0]].append(edge[1])
            self.neighbors[edge[1]].append(edge[0])

    def neighbor_matrix(self):
        first_line = " ".join([str(i + 1) for i in range(self.vertices)])
        print(" " * (len(str(self.vertices)) + 1) + first_line)
        print(" " * (len(str(self.vertices)) + 1) + "_" * len(first_line))
        for i in range(self.vertices):
            print(f"{i + 1:>{len(str(self.vertices))}}|", end="")
            st = ""
            for j in range(self.vertices):
                if j + 1 in self.neighbors[i + 1]:
                    st += "1 "
                else:
                    st += "0 "
            print(st)

class Tree(Graph):
    def find_tree_center(self):
        while len(self.neighbors.keys()) > 2:
            to_del = []
            for vertex in self.neighbors.keys():
                if len(self.neighbors[vertex]) <= 1:
                    to_del.append(vertex)
            for deletion in to_del:
                del self.neighbors[deletion]
            for vertex, neighbors in self.neighbors.items():
                for deletion in to_del:
                    if deletion in neighbors:
                        neighbors.remove(deletion)
        if len(self.neighbors.keys()) == 0:
            return "No vertices!"
        elif len(self.neighbors.keys()) == 1:
            return f"Center made of one vertex: {list(self.neighbors.keys())[0]}"
        else:
            return f"Center made of two vertices: {list(self.neighbors.keys())[0]}, {list(self.neighbors.keys())[1]}"
    
    
    def create_code(self, root, ignore=None):
        # base case - leaf
        if len(self.neighbors[root]) == 1:
            del self.neighbors[root]
            for vertex, neighbors in self.neighbors.items():
                if root in neighbors:
                        neighbors.remove(root)
            return "01"
        children = sorted([i for i in self.neighbors[root] if i != ignore])
        code = ""
        for child in children:
            code += self.create_code(child, root)
        return "0" + code + "1"

        
