# undirected graph:
def isCycle(self, V: int, adj: List[List[int]]) -> bool:
            #Code here
            vis = [0]*V
            def dfs(x,parent):
                vis[x] = 1
                for i in adj[x]:
                    if vis[i] == 0:
                        if dfs(i,x):
                            return True
                    else:
                        if parent!=i:
                            return True
                return False
                
                
            for i in range(V):
                if vis[i] == 0:
                    if dfs(i,-1):
                        return True
            return False


from typing import List
from collections import deque
class Solution:
    #Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        #Code here
        vis = [0]*V
        def bfs(x):
            q = deque()
            q.append((x,-1))
            vis[x] = 1
            while q:
                node = q.popleft()
                x = node[0]
                parent = node[1]
                for i in adj[x]:
                    if vis[i] == 0:
                        vis[i] = 1
                        q.append((i,x))
                    else:
                        if i!=parent:
                            return True
            return False
        for i in range(V):
            if vis[i] == 0 and bfs(i) == True:
                return True
        return False
            
            
# directed graph: backtracking path visited and visited
def isCyclic(self, V : int , adj : List[List[int]]) -> bool :
        pathvis = [0]*V
        vis = [0]*V
        
        def dfs(node):
            for i in adj[node]:
                if vis[i] == 0:
                    vis[i] = 1
                    pathvis[i] = 1
                    if dfs(i):
                        return True
                elif pathvis[i] == 1:
                    return True
            pathvis[node] = 0
            return False
        for i in range(V):
            if vis[i] == 0:
                vis[i] = 1
                pathvis[i] = 1
                if dfs(i) == True:
                    return True
        return False

#directed graph using toposort(kahns algo)
from typing import List
from collections import deque
class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V : int , adj : List[List[int]]) -> bool :
        indegree = [0]*V
        for i in range(V):
            for j in adj[i]:
                indegree[j]+=1
        q = deque()
        for i in range(V):
            if indegree[i] == 0:
                q.append(i)
        cnt = 0
        while q:
            node = q.popleft()
            cnt+=1
            for i in adj[node]:
                indegree[i]-=1
                if indegree[i] == 0:
                    q.append(i)
        return cnt!=V
