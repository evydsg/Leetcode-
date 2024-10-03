def findPath(start, end, paths):
    graph = {}

    # Build the graph
    for start_node, end_node in paths:
        if start_node in graph:
            graph[start_node].add(end_node)  # Add to set
        else:
            graph[start_node] = {end_node}  # Initialize a set with end_node
    
    # DFS function to find all paths from start to end
    def dfsAllPaths(start, end):
        all_paths = []
        currentPath = []

        def dfs(node):
            currentPath.append(node)

            if node == end:
                all_paths.append(currentPath.copy())  # Append a copy of the current path
            else:
                for neighbor in graph.get(node, []):
                    if neighbor not in currentPath:  # Avoid cycles
                        dfs(neighbor)

            currentPath.pop()  # Backtrack
        
        # Start DFS from the start node
        dfs(start)
        return all_paths

    # Call the DFS function to find all paths
    return dfsAllPaths(start, end)
