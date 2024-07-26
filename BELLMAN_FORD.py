def bellman_ford(self, V, edges, S):
        dis = [10**8]*V
        dis[S] = 0
        for i in range(V-1):
            for a,b,d in edges:
                if dis[a]!=10**8 and dis[a]+d<dis[b]:
                    dis[b] = dis[a]+d
        #used for detecting negative edges
        for a,b,d in edges:
            if dis[a]!=10**8 and dis[a]+d<dis[b]:
                return [-1]
        return dis
