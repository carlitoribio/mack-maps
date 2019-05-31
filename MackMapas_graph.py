#!/usr/bin/env python
# coding: utf-8

# In[16]:


from collections import deque, namedtuple

inf = float('inf')
Edge = namedtuple('Edge', 'start, end, cost')


def make_edge(start, end, cost=1):
  return Edge(start, end, cost)


class Graph:
    def __init__(self, edges):
        wrong_edges = [i for i in edges if len(i) not in [2, 3]]
        if wrong_edges:
            raise ValueError('Wrong edges data: {}'.format(wrong_edges))

        self.edges = [make_edge(*edge) for edge in edges]

    @property
    def vertices(self):
        return set(
            sum(
                ([edge.start, edge.end] for edge in self.edges), []
            )
        )

    def get_node_pairs(self, n1, n2, both_ends=True):
        if both_ends:
            node_pairs = [[n1, n2], [n2, n1]]
        else:
            node_pairs = [[n1, n2]]
        return node_pairs

    def remove_edge(self, n1, n2, both_ends=True):
        node_pairs = self.get_node_pairs(n1, n2, both_ends)
        edges = self.edges[:]
        for edge in edges:
            if [edge.start, edge.end] in node_pairs:
                self.edges.remove(edge)

    def add_edge(self, n1, n2, cost=1, both_ends=True):
        node_pairs = self.get_node_pairs(n1, n2, both_ends)
        for edge in self.edges:
            if [edge.start, edge.end] in node_pairs:
                return ValueError('Edge {} {} already exists'.format(n1, n2))

        self.edges.append(Edge(start=n1, end=n2, cost=cost))
        if both_ends:
            self.edges.append(Edge(start=n2, end=n1, cost=cost))

    @property
    def neighbours(self):
        neighbours = {vertex: set() for vertex in self.vertices}
        for edge in self.edges:
            neighbours[edge.start].add((edge.end, edge.cost))

        return neighbours

    def dijkstra(self, source, dest):
        print(source, dest)
        assert source in self.vertices, 'Such source node doesn\'t exist'
        assert source is not dest, 'Source must differ from destination'
        streets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q"]
        assert source not in streets, 'Source can\'t be street'
        assert dest not in streets, 'Destination can\'t be street'
        distances = {vertex: inf for vertex in self.vertices}
        previous_vertices = {
            vertex: None for vertex in self.vertices
        }
        distances[source] = 0
        vertices = self.vertices.copy()

        while vertices:
            current_vertex = min(
                vertices, key=lambda vertex: distances[vertex])
            vertices.remove(current_vertex)
            if distances[current_vertex] == inf:
                break
            for neighbour, cost in self.neighbours[current_vertex]:
                alternative_route = distances[current_vertex] + cost
                if alternative_route < distances[neighbour]:
                    distances[neighbour] = alternative_route
                    previous_vertices[neighbour] = current_vertex

        path, current_vertex = deque(), dest
        while previous_vertices[current_vertex] is not None:
            path.appendleft(current_vertex)
            current_vertex = previous_vertices[current_vertex]
        if path:
            path.appendleft(current_vertex)
        return path


graph = Graph([
    ("c1", "a", 1), ("a", "c1", 1),  
    ("a", "b", 1),  ("b", "a", 1),
    ("b", "c", 1), ("c", "b", 1),
    ("c", "p33", 1), ("p33", "c", 1),
    ("c", "d", 1), ("c", "d", 1),
    ("d", "p30", 1), ("p30", "d", 1), 
    ("d", "e", 1),  ("e", "d", 1),
    ("e", "p31", 1), ("p31", "e", 1),
    ("e", "f", 1), ("f", "e", 1),
    ("e", "g", 1), ("g", "e", 1),
    ("f", "h", 1), ("h", "f", 1),
    ("f", "i", 1), ("i", "f", 1),
    ("g", "i", 1), ("i", "g", 1),
    ("g", "j", 1), ("j", "g", 1),
    ("h", "i", 1), ("i", "h", 1),
    ("h", "k", 1), ("k", "h", 1),
    ("i", "l", 1), ("l", "i", 1),
    ("j", "m", 1), ("m", "j", 1),
    ("k", "n", 1), ("n", "k", 1),
    ("k", "o", 1), ("o", "k", 1),
    ("l", "m", 1), ("m", "l", 1),
    ("l", "o", 1), ("o", "l", 1),
    ("m", "p", 1), ("p", "m", 1),
    ("n", "c2", 1), ("c2", "n", 1),
    ("o", "p46", 1), ("p46", "o", 1),
    ("p", "q", 1), ("q", "p", 1),
    ("q", "p19", 1), ("p19", "q", 1)])


# In[17]:


#test

graph.dijkstra("p33", "c1")

