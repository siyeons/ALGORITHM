def findItinerary(self, tickets: List[List[str]]) -> List[str]:
    graph = collections.defaultdict(list)

    for a, b in sorted(tickets):
        graph[a].append(b)

    route = []
    def dfs(a, root):
        visited = []
        stack = [root]

        while(stack):
            node = stack.pop()
            if (node not in visited):
                visited.append(node)
                stack.extend(graph[node])
        return visited

    answer = dfs(graph, 'JFK')

 return answer