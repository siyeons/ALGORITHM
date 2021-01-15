class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = collections.defaultdict(list)
        
        for x, y in prerequisites:
            graph[x].append(y)
            
        traced = set()
        
        def dfs(i):
            if i in traced:
                return False
            traced.add(i)
            
            for y in graph[i]:
                if not dfs(y):
                    return False
                
            traced.remove(i)
                
            return True
            
        for x in list(graph):
            if not dfs(x):
                return False
            
        return True
    
    
    #better solution
    
def canFinish(self, numCourses):
    	graph = [[] for _ in range(numCourses)]
visited = [0 for _ in range(numCourses)]

for pair in prerequisites:
            a, b = pair
            graph[a].append(b)

for i in range(numCourses):
	if not self.dfs(graph, visited, i):
		return False

return True

def dfs(self, graph, visited, i):
	if visited[i] == -1:
		return False
	if visited[i] == 1:
		return True

	# 방문했다고 변경
	visited[i] = -1
	
	for j in graph[i]:
		if not self.dfs(graph, visited, j):
			return False

	# 모든 행선지를 다 방문했으면 1로 변경
	visited[1] = 1
	return True