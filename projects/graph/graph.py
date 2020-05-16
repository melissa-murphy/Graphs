"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        # create set of vertices
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        # add edges and their associated vertexes
        if v1 in self.vertices and v2 in self.vertices:
            # v2 is one of the things that v1 connects to
            self.vertices[v1].add(v2)
        else:
            raise IndexError("Vertex does not exist in graph")

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    # def bft(self, starting_vertex):
    #     # add starting node to a queue
    #     q = Queue()
    #     q.enqueue(starting_vertex)

    #     # track visited nodes
    #     visited = set()

    #     # while queue isnt empty:
    #     while q.size() > 0:
    #         # if the vert hasnt been visited:
    #         # dequeue the first vertex
    #         v = q.dequeue()
    #         # if it is not visited print vertex
    #         if v not in visited:
    #             print(v)
    #             # and then mark as visited
    #             visited.add(v)
    #             # add neighbors not already visited to queue and repeat

    #             for next_vertex in self.get_neighbors(v):
    #                 q.enqueue(next_vertex)

    # def dft(self, starting_vertex):
    #     # add starting node to stack
    #     s = Stack()

    #     # track visited
    #     visited = set()

    #     # while stack isn't empty:
    #     while s.size() > 0:
    #         # pop the first vert
    #         v = s.pop()
    #         # if that vert isnt visited:
    #         if v not in visited:
    #             print(v)
    #             # mark as visited
    #             visited.add(v)
    #     # add all unvisited neighbors to the stack
    #         for next_vertex in self.get_neighbors(v):
    #             s.push(next_vertex)

    # def dft_recursive(self, starting_vertex, visited=None, path=None):
    #     # print starting vert (None)
    #     print(starting_vertex)

    #     # if visited is None, create new set
    #     if visited is None:
    #         visited = set()

    #     # add visited to starting_vertex
    #     visited.add(starting_vertex)

    #     # for each child starting_vertex:
    #     for child_vertex in self.vertices[starting_vertex]:
    #         # if child is not in visited, perform dft_recursive on child vert
    #         if child_vertex not in visited:
    #             self.dft_recursive(child_vertex, visited)

    def bfs(self, starting_vertex, destination_vertex):
        # add starting node to a queue
        q = Queue()
        q.enqueue([starting_vertex])

        # track visited nodes
        visited = set()

        # while queue isnt empty:
        while q.size() > 0:
            # if the vert hasnt been visited:
            # dequeue the first vertex
            v = q.dequeue()
            last_v = v[-1]
            # if it is not visited print vertex
            if last_v not in visited:
                if v == destination_vertex:
                    return v
                else:
                    # mark as visited
                    visited.add(last_v)
                    # add neighbors not already visited to queue and repeat
                    neighbors = self.get_neighbors(last_v)

                    for neighbor in neighbors:
                        v_copy = v[:]
                        v_copy.append(neighbors)
                        q.enqueue(v_copy)

    # def dfs(self, starting_vertex, destination_vertex):
    #     """
    #     Return a list containing a path from
    #     starting_vertex to destination_vertex in
    #     depth-first order.
    #     """
    #     pass  # TODO

    # def dfs_recursive(self, starting_vertex, destination_vertex):
    #     """
    #     Return a list containing a path from
    #     starting_vertex to destination_vertex in
    #     depth-first order.

    #     This should be done using recursion.
    #     """
    #     pass  # TODO


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
