import random

class NeighborsGraph:
    def __init__(self, vertices=None, edges=None):
        self.vertices = vertices or {}
        if edges:
            for edge in edges:
                self.add_edge(edge[0], edge[1])


    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices:
            self.vertices[vertex1].append(vertex2)
        else:
            self.vertices[vertex1] = [vertex2]

        if vertex2 in self.vertices:
            self.vertices[vertex2].append(vertex1)
        else:
            self.vertices[vertex2] = [vertex1]

def partition(G):

    def group_improved(G, A, B):

        improved = False
        
        for vertex in A:
            gain = 0
            for neighbor in G.vertices[vertex]:
                if neighbor in B:
                    gain -= 1
                elif neighbor in A:
                    gain += 1

            
            if gain > 0:
                A.remove(vertex)
                B.append(vertex)
                improved = True
        
        return improved

    vertices = list(G.vertices.keys())
    random.shuffle(vertices)
    A = vertices[:len(vertices)//2]
    B = vertices[len(vertices)//2:]

    
    while True:
        
        improved_A = group_improved(G, A, B)
        improved_B = group_improved(G, B, A)

        if not (improved_A or improved_B):
            break

    removed_edges = 0
    for v in G.vertices.keys():
        neighbors = G.vertices[v]
        for w in neighbors:
            if (v in A and w in A) or (v in B and w in B):
                removed_edges += 1


    return A, B, removed_edges

if __name__ == '__main__':

    G = NeighborsGraph()
    # Test partition method
    G.add_vertex(1)
    G.add_vertex(2)
    G.add_vertex(3)
    G.add_vertex(4)
    G.add_vertex(5)
    G.add_edge(1, 2)
    G.add_edge(1, 3)
    G.add_edge(1, 4)
    G.add_edge(1, 5)

    groups_edges_count = partition(G)
    print(groups_edges_count)

    