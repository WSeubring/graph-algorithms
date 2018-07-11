from Vertex import Vertex


class Graph:
    def __init__(self, is_directed=True):
        self.name = None
        self.vertexes = dict()
        self.is_directed = is_directed
        self.n_edges = 0
        self.count = 0

    def add_vertex(self, name):
        self.vertexes[str(name)] = Vertex(name)

    def add_edge(self, from_vertex, to_vertex):
        # todo: add check to see if the vertexes exist
        self.n_edges += 1
        vertex_a = self.vertexes[str(from_vertex)]
        vertex_b = self.vertexes[str(to_vertex)]

        vertex_a.add_neighbour(vertex_b)
        if not self.is_directed:
            vertex_b.add_neighbour(vertex_a)

    def dfs(self, vertex_name_a, vertex_name_b):
        self.count = 0
        self.reset_visited_vertexes()

        begin_vertex = self.vertexes[str(vertex_name_a)]
        target = self.vertexes[str(vertex_name_b)]

        path = self.__dfs_recursion(begin_vertex, target, "[")
        if path is not None:
            path = path[:-2] + "]"
            return path

        return None

    def __dfs_recursion(self, vertex, target, path):
        path += "{}->".format(str(vertex.name))

        vertex.visited = True
        vertex.pre = self.count
        self.count += 1

        if vertex == target:
            return path

        for next_vertex in vertex.connections_to:
            if not next_vertex.visited:
                return self.__dfs_recursion(next_vertex, target, path)

        for possible_vertex_other_cluster in self.vertexes.values():
            if not possible_vertex_other_cluster.visited:
                return self.__dfs_recursion(possible_vertex_other_cluster, target, "[")

        vertex.post = self.count
        self.count += 1

    def num_of_clusters(self):
        if len(self.vertexes) == 0:
            return 0

        starting_vertex = self.vertexes["1"]

        return 1 + self.__num_of_clusters_recursion(starting_vertex)

    def __num_of_clusters_recursion(self, vertex):
        vertex.visited = True
        for next_vertex in vertex.connections_to:
            if not next_vertex.visited:
                return self.__num_of_clusters_recursion(next_vertex)

        for possible_vertex_other_cluster in self.vertexes.values():
            if not possible_vertex_other_cluster.visited:
                return 1 + self.__num_of_clusters_recursion(possible_vertex_other_cluster)

        return 0

    def reset_visited_vertexes(self):
        for vertex in self.vertexes:
            vertex.visited = False

    def __str__(self):
        text = ""
        for item in self.vertexes:
            text += '{} -> ['.format(item)

            for vertex in self.vertexes[item].connections_to:
                text += "{}, ".format(str(vertex.name))
                pass
            text += ']\n'
        return text


