class Graph:
    def __init__(self, adj):
        self.adj = adj
    
    def _dfs_path(self, current, target, visited):
        if current == target:
            return True
        visited[current] = True
        for neighbour in self.adj[current]:
            if not visited[neighbour]:
                if self._dfs_path(neighbour, target, visited):
                    return True
        return False
    
    def has_path(self, start, end):
        visited = [False] * len(self.adj)
        return self._dfs_path(start, end, visited)

    def is_fully_connected(self):
        visited = [False] * len(self.adj)
        self._dfs_path(0, 0, visited)

        for node in visited:
            if node == False:
                return False
            else:
                return True


graph = Graph([    [1, 2]   ,[0, 2],    [0, 1, 3],    [2]])
print(graph.is_fully_connected())