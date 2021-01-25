"""
Implement a graph

- weighted OR unweighted:
    Vertices - have weights
    Edges    - have weights (weights - not the same in both directions)
- directed AND undirected:
    n.b.: one way and two way
- adjacency list
"""


class Vertex:

    def __init__(self, name):
        self.name = name
        self.weight = 0  # vertex weight
        self.neighbors = {}  # {Vertex: edge_weight}

    def add_neighbor(self, vertex, edge_weight: int = 0):
        """Adds neighbor vertex and its weight to the neighbors dict"""
        if vertex not in self.neighbors:
            self.neighbors[vertex] = edge_weight

    # def get_connections(self):
    #     return self.neighbors.keys()
    #
    # def get_edge_weight(self, neighbor):
    #     return self.neighbors[neighbor]


class Graph:

    # store all the vertices in the graph:
    vertices_dict: dict = {}  # {Vertex.name: Vertex}

    vertices_nr: int = 0
    edge_nr: int = 0

    def add_vertex(self,
                   vertex: Vertex,
                   vertex_weight: int = 0):

        # if 1. vertex is of Vertex class AND
        #    2. vertex name is not already present in the dict
        #       that contains all vertices in the graph
        if isinstance(vertex, Vertex) and \
                vertex.name not in self.vertices_dict:

            self.vertices_dict[vertex.name] = vertex
            vertex.weight = vertex_weight  # setting the weight of the vertex
            self.vertices_nr += 1
            return True

        return False

    def add_edge(self,
                 v,  # source vertex
                 u,  # destination vertex
                 edge_weight_v_to_u: int = 0,
                 edge_weight_u_to_v: int = 0,
                 two_way: bool = False):
        """Adds edge between vertices

        Meaning that:
        A. Unidirectional graphs:
            the destination vertex (u) is added to the
            neighbors dict of the source vertex (v) - one way vertex

        B. Bidirectional graphs:
            u - added to v neighbors dict
            v - added to u neighbors dict
        """

        # if u and v exist in graph - add the edge between them:
        if u in self.vertices_dict and v in self.vertices_dict:
            self.vertices_dict[v].add_neighbor(u, edge_weight_v_to_u)

            # if the edge is two-way - add reverse connection:
            if two_way:
                self.vertices_dict[u].add_neighbor(v, edge_weight_u_to_v)

            return True

        return False

    def print_graph(self):
        for vertex in self.vertices_dict.keys():
            print(f'{vertex}({self.vertices_dict[vertex].weight}) - '
                  f'{self.vertices_dict[vertex].neighbors}')


# =====================================================================
#                               --- TEST ---
# =====================================================================

if __name__ == '__main__':
    import random
    g = Graph()
    for i in range(ord('A'), ord('K')):
        vertex_w = random.randint(0, 9)
        g.add_vertex(Vertex(chr(i)), vertex_weight=vertex_w)

    edges = {'AB': (3, 5, 1), 'AE': (2, 7, 1), 'BF': (4, 9, 1),
             'CG': (15, 2, 1), 'DE': (5, 7, 1), 'DH': (5, 5, 1),
             'EH': (8, 7, 1), 'CE': (6, 1, 1), 'FG': (10, 10, 1),
             'FI': (5, 8, 1), 'FJ': (4, 1, 1), 'HI': (4, 6, 1)}
    for edge, val in edges.items():

        g.add_edge(edge[0],
                   edge[1],
                   edge_weight_v_to_u=val[0],
                   edge_weight_u_to_v=val[1],
                   two_way=val[2])

    g.print_graph()
