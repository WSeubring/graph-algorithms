import math

class Vertex:
    def __init__(self, name):
        self.name = name
        self.connections_to = []
        self.visited = False
        self.prev = None
        self.pre = None
        self.post = None

    def add_neighbour(self, neighbour):
        self.connections_to.append(neighbour)
