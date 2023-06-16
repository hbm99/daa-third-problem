from collections import deque
class Graph():
        
    def __init__(self, vertices, graph = None):
        self.V = vertices
        self.graph = graph or  [[0 for column in range(vertices)] for row in range(vertices)]
        self.colorArr = [-1 for i in range(self.V)]
        self.distances = {v: [0] * self.V for v in range(self.V)}

    # BFS
 
    def is_bipartite_util_bfs(self, src):
 
        # Create a color lst to store colors
        # assigned to all vertices. Vertex
        # number is used as index in this lst.
        # The value '-1' of self.colorArr[i] is used
        # to indicate that no color is assigned to
        # vertex 'i'. The value 1 is used to indicate
        # first color is assigned and value 0
        # indicates second color is assigned.
 
        # Assign first color to source
 
        # Create a queue (FIFO) of vertex numbers and
        # enqueue source vertex for BFS traversal
        queue = []
        queue.append(src)
 
        # Run while there are vertices in queue
        # (Similar to BFS)
        while queue:
 
            u = queue.pop()
 
            # Return false if there is a self-loop
            if self.graph[u][u] == 1:
                return False
 
            for v in range(self.V):
 
                # An edge from u to v exists and
                # destination v is not colored
                if (self.graph[u][v] == 1 and
                        self.colorArr[v] == -1):
 
                    # Assign alternate color to
                    # this adjacent v of u
                    self.colorArr[v] = 1 - self.colorArr[u]
                    queue.append(v)
 
                # An edge from u to v exists and destination
                # v is colored with same color as u
                elif (self.graph[u][v] == 1 and
                      self.colorArr[v] == self.colorArr[u]):
                    return False
 
        # If we reach here, then all adjacent
        # vertices can be colored with alternate
        # color
        return True
 
    def is_bipartite_bfs(self):
        self.colorArr = [-1 for i in range(self.V)]
        for i in range(self.V):
            if self.colorArr[i] == -1:
                if not self.is_bipartite_util_bfs(i):
                    return False
        return True

    def bfs_tree(self, s):
        visited = [False] * self.V
        parent = [-1] * self.V
        level = [-1] * self.V
        queue = deque()

        visited[s] = True
        level[s] = 0
        queue.append(s)

        while queue:
            u = queue.popleft()
            for v in range(len(self.graph[u])):
                if self.graph[u][v] == 1 and not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    level[v] = level[u] + 1
                    queue.append(v)

        bfs_tree = {}
        for i in range(self.V):
            if parent[i] != -1:
                bfs_tree[i] = parent[i]

        return bfs_tree
    
    # DFS

    def color_graph(self, color, pos, c):
        if color[pos] != -1 and color[pos] != c:
            return False
        
        color[pos] = c
        ans = True
        for i in range(0, self.V):
            if self.graph[pos][i]:
                if color[i] == -1:
                    ans &= self.color_graph(color, i, 1 - c)
                    
                if color[i] != -1 and color[i] != 1 - c:
                    return False
            
            if not ans:
                return False
        
        return True
    
    def is_bipartite_dfs(self):
        color = [-1] * self.V
        #start is vertex 0
        pos = 0
        # two colors 1 and 0
        for pos in range(self.V):
            if color[pos] == -1:
                result = self.color_graph(color, pos, 1)
                if not result:
                    return False
        return True

    #############################

    def unweighted_floyd_warshall(self):
        for i in range(self.V):
            for j in range(self.V):
                if self.graph[i][j] != 0:
                    self.distances[i][j] = self.graph[i][j]

        for k in range(self.V):
            for i in range(self.V):
                for j in range(self.V):
                    if i != j and i != k and j != k:
                        if self.distances[i][k] != 0 and self.distances[k][j] != 0:
                            dist = self.distances[i][k] + self.distances[k][j]
                            if self.distances[i][j] == 0:
                                self.distances[i][j] = dist

        return self.distances
    

    