max_in_window():
    max_arr = [1...n]
    heap = initialize_max_heap( (i, A[i]) for i in range 0...k )

    for i in 1...n:
        max[i] = heap.peak()

        heap.remove(key=i)
        if (i + 1 + k <= n):
            heap.insert((i+1+k, A[i+1+k])) 


Modified_Dijckstras():
    dist = [ set all nodes to infinity ]
    prev = [ set all nodes to None ]
    dist[s] = weight[s]

    H = initialize_min_heap(dist)

    while H is not empty:
        u = H.removeMin()
        for edge (u, v) in E:
            potential_dist = dist[u] + length(u, v) + weight[v]
            if potential_dist < dist[v]:
                dist[v] = potential_dist
                H.update_heapify(v, potential_dist)
                prev[v] = u
