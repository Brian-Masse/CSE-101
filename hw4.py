max_in_window():
    max_arr = [1...n]
    heap = initialize_max_heap( (i, A[i]) for i in range 0...k )

    for i in 1...n:
        max[i] = heap.peak()

        heap.remove(key=i)
        if (i + 1 + k <= n):
            heap.insert((i+1+k, A[i+1+k])) 

