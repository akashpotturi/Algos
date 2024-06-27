def shortestPath(self, n : int, m : int, edges : List[List[int]]) -> List[int]:
        
        adj = [[] for _ in range(n)]
        for i in range(m):
            u = edges[i][0]
            v = edges[i][1]
            wt = edges[i][2]
            adj[u].append((v,wt))
            
        vis = [0]*n
        s = []
        
        def toposort(i):
            for node in adj[i]:
                j = node[0]
                if vis[j] == 0:
                    vis[j] = 1
                    toposort(j)
            s.append(i)
            
        for i in range(n):
            if vis[i] == 0:
                vis[i] = 1
                toposort(i)
                
        dis = [float('inf')]*n
        src = 0
        s.reverse()
        dis[src] = 0
        for i in s:
            for node in adj[i]:
                v = node[0]
                wt = node[1]
                if dis[i]+wt<dis[v]:
                    dis[v] = dis[i]+wt
        for i in range(n):
            if dis[i] == float('inf'):
                dis[i] = -1
        return dis