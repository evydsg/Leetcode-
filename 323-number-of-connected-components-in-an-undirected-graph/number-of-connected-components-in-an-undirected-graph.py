class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
            Understand
                - Find how many nodes are connect in the graph

                Question
                    - Can we get a graph that no nodes are connected at all?
                    - Can we get an empty list?

            Match
                - DFS
            
            Plan
                Create an adjacency list from the given edges.
                Initialize a visited list to keep track of visited nodes.
                Iterate through each node, and if the node has not been visited, perform a DFS and increment the component count.    

        """
        
        def dfs(node):
            stack = [node]

            while stack:
                current = stack.pop()
                for neighbor in graph[current]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        stack.append(neighbor)
        
        components = 0

        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = [False] * n #List to keep track of visited nodes

        components = 0

        for i in range(n):
            if not visited[i]:
                visited[i] = True
                dfs(i)

                components += 1
        
        return components
