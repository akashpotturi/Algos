def topoSort(self, V, adj):
    # Code here
    ans = []
    vis = [0]*V
    def dfs(node):
        for i in adj[node]:
            if vis[i] == 0:
                vis[i] = 1
                dfs(i)
        ans.append(node)
    for i in range(V):
        if vis[i] == 0:
            vis[i] = 1
            dfs(i)
    return ans.reverse()
from collections import deque
def topoSort(self, V, adj):
        # Code here
        q = deque()
        indegree = [0]*V
        for i in range(V):
            for j in adj[i]:
                indegree[j]+=1
        for i in range(V):
            if indegree[i] == 0:
                q.append(i)
        ans = []
        while q:
            node = q.popleft()
            ans.append(node)
            for i in adj[node]:
                indegree[i]-=1
                if indegree[i] == 0:
                    q.append(i)
        return ans