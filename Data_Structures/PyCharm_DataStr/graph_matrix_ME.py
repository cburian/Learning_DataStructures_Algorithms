"""
Implement a graph

- weighted OR unweighted
- directed AND undirected:
    n.b.: one way and two way
- adjacency matrix
"""


class Vertex:

    def __init__(self, name):
        self.name = name
        self.weight = 0
        self.neighbors = {}  # {Vertex: edge_weight}

    def add_neighbor(self, vertex, edge_weight):
        if vertex not in self.neighbors:
            self.neighbors[vertex] = edge_weight

    @property
    def weight(self):
        return self.weight

    @weight.setter
    def weight(self, weight):
        self.weight = weight


class Graph:

    vertices_dict = {}  # {Vertex.name: Vertex}
    vertices_nr = 0
    edge_nr = 0

    def add_vertex(self,
                   vertex: Vertex,
                   vertex_weight: int = 0):

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

        if u in self.vertices_dict and v in self.vertices_dict:
            for vertex_name, vertex in self.vertices_dict.items():
                if vertex_name == v:
                    vertex.add_neighbor(u, edge_weight_v_to_u)
                if two_way:
                    if vertex_name == u:
                        vertex.add_neighbor(v, edge_weight_u_to_v)
            return True
        return False
