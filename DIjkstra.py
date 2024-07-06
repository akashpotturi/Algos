def dijkstra(self, V, adj, S):
        #code here
        import heapq
        dis = [10**9]*V
        dis[S] = 0
        heap = []
        heapq.heappush(heap,(0,S))
        while heap:
            node = heapq.heappop(heap)
            d = node[0]
            x = node[1]
            for i in adj[x]:
                edgewt = i[1]
                adjnode = i[0]
                if dis[adjnode]>d+edgewt:
                    dis[adjnode] = d+edgewt
                    heapq.heappush(heap,(dis[adjnode],adjnode))
        return dis
