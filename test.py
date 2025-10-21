def shortestPath(s, t):
    dist: dict[label: int] = []     # create a dictionary for initial distances
    prev: dict[label: label] = []   # Create a dictionary for previous nodes

    for v in S:
        dist[v] = infinity
    dist[s] = 0

    F = createHeap(S)               # initialize the min-heap with all verticies, ordered by distance

    while (F not empty):
        v = F.removeMin()           # pull the vertex with the shortest path, O(logn)
        
        for u in neighborhood(v) and u not in F:

            # Using an additional array to store the location of labels in the min-heap
            # Such an array makes finding certain nodes O(1)
            if F.find(u) > F.find(v) + l(v, u):
                F.FindAndLower(u, F.find(v) + l(v, u))
                prev[u] = v
    
            if v == t:
                # Returning the previous allows the calling function to reconstruct
                # the path from s to t, by following prev[t] until reaching s. 
                return prev