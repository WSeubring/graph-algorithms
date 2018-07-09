from Graph import Graph

testCases_dfs = \
    [
        [4, 4], [1, 2], [3, 2], [4, 3], [1, 4], [1, 4], [1]
    ],\
    [
        [4, 2], [1, 2], [3, 2], [1, 4], [0]
    ],\
    [
        [4, 4], [1, 2], [3, 4], [3, 4], [1]
    ]

testCases_noc = \
    [
        [4, 4], [1, 2], [3, 2], [4, 3], [1, 4], [1]
    ],\
    [
        [4, 2], [1, 2], [3, 2], [2]
    ],\
    [
        [4, 2], [1, 2], [3, 4], [2]
    ],\
    [
        [10, 0], [10]
    ]


def create_graph(input):
    tmp_graph = Graph(is_directed=False)
    nVertexes = input[0][0]
    nEdges = input[0][1]

    for i in range(1, nVertexes + 1):
        tmp_graph.add_vertex(name=i)

    edges = input[1:-2]
    for edge in edges:
        tmp_graph.add_edge(from_vertex=edge[0], to_vertex=edge[1])

    return tmp_graph


def run__dfs_test_cases():
    counter = 0
    for testCase in testCases_dfs:
        counter += 1
        # Create a undirected graph
        graph = create_graph(testCase)

        expected_result = testCase[-1][0]
        vertex_name_a = testCase[-2][0]
        vertex_name_b = testCase[-2][1]
        path = graph.dfs(vertex_name_a, vertex_name_b)

        result = 0
        if path is not None:
            result = 1
            print(path + " : ", end="")

        if result == expected_result:
            print("TestCase{}: was successful ({} connected to {} -> {})".format(counter, vertex_name_a, vertex_name_b, expected_result))
        else:
            print("TestCase{}: was not successful ({} connected to {} -> {})".format(counter, vertex_name_a, vertex_name_b,

                                                                                 expected_result))
def run__num_clusters_test_cases():
    counter = 0
    for testCase in testCases_noc:
        counter += 1
        # Create a undirected graph
        graph = create_graph(testCase)
        if len(testCase) > 2:
            graph.add_edge(testCase[-2:-1][0][0], testCase[-2:-1][0][1])

        expected_result = testCase[-1][0]
        result = graph.num_of_clusters()

        if result == expected_result:
            print("TestCase{}: was successful ({})".format(counter, result))
        else:
            print("TestCase{}: was not successful ({} num of graphs should be  -> {})".format(counter, result,
                                                                                          expected_result))


def main():
    run__dfs_test_cases()
    run__num_clusters_test_cases()
    pass

main()
