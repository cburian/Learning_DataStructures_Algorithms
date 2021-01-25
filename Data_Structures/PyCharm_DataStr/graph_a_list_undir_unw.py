"""
Implementation of:

Graph:
    - undirected
    - unweighted
    - adjacency list - stored in vertex

Resources:
https://www.youtube.com/watch?v=HDUzBEG1GlA&ab_channel=JoeJames
"""


class Vertex:
    def __init__(self, n):
        self.name = n
        self.neighbors = []

    def add_neighbor(self, vertex):
        if vertex not in self.neighbors:
            self.neighbors.append(vertex)
            self.neighbors.sort()


class Graph:
    vertices = {}

    def add_vertex(self, vertex: Vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True

        return False

    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            for key, val in self.vertices.items():
                if key == u:
                    val.add_neighbor(v)
                if key == v:
                    val.add_neighbor(u)
            return True
        return False

    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(f'{key} - {str(self.vertices[key].neighbors)}')


# test:
if __name__ == '__main__':

    g = Graph()
    print(len(g.vertices))
    a = Vertex('A')
    g.add_vertex(a)
    g.add_vertex(Vertex('B'))
    for i in range(ord('A'), ord('K')):
        g.add_vertex(Vertex(chr(i)))

    edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH',
             'EH', 'AE', 'FG', 'FI', 'FJ', 'HI']
    for edge in edges:
        g.add_edge(edge[0], edge[1])

    g.print_graph()
    print(g.vertices.items())
