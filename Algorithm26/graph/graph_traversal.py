from collections import deque
class Graph:
    def __init__(self,):
        num_nodes, num_edges = map(int,input().split())
        self.bidirection = int(input('양방향 : 1, 단방향 : 0 = '))
        self.graph = [[]for _ in range(num_nodes+1)]
        for _ in range(num_edges):
            u,v = map(int,input().split())
            self.graph[u].append(v)
            if self.bidirection:
                self.graph[v].append(u)

        self.visited = []
    
    def dfs(self, node):
        print(node, end=' ')
        self.visited.append(node)
        for adj_node in self.graph[node]:
            if adj_node not in self.visited:
                self.dfs(adj_node)

    def bfs(self, start):
        visited = []
        queue = deque()
        queue.append(start)
        visited.append(start)
        print(start, end=' ')

        while queue:
            prev_node = queue.popleft()
            for node in self.graph[prev_node]:
                if node not in visited:
                    prev_node.append(node)
                    visited.append(node)
                    print(node, end=' ')


if __name__ == '__main__':
    g = Graph()
    start = int(input('시작 노드 번호 :'))
    g.dfs(start)
    print('\n')
    g.visited.clear()
    g.bfs(start)
    print()

