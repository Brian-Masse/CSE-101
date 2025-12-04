# MARK: bus_stops
def bus_stops(BR1...BRn, curr, m):

    # there may not be a valid path from every point i to m,
    # so fill all spots except the ending 
    cost = [ infinity ]
    cost[m] = 0

    for k from m - 1 to 1:
        for all BRi in BR1...BRn such that si <= k < fi:
            cost[k] = min(cost[k], ci + cost[fi])
    
    return cost[1]


# MARK: MWCS
def MWCS(root, k) -> smallest:

    # if a subtree does not contain k nodes (ie. does not satisfy constraints of potential solution)
    # return infinity
    smallest = infinity
    weight = [infinity]
    size = [infinity]

    for v in (post-order traverse root):
        if |v.children| == 0:
            weight[v] = v.value
            size[v] = 1
        
        if |v.children| == 1:
            weight[v] = v.value + weight[v.child]
            size[v] = 1 + size[v.child]

        else:
            weight[v] = v.value + weight[lc.v] + weight[rc.v]
            size[v] = 1 + size[lc.v] + size[rc.v]
        
        # attempt to update the variable for subtrees satisfying problem constraints
        if size[v] == k:
            smallest = min(smallest, weight[v])
    
    return smallest

# MARK: KV()
def KV(I1,...In, U):

    sort (I1,...In) by the value ratio of each item

    # create memoized arrays
    U' = [infinity]; U'[0] = U
    V = [0]
    P = [0]

    # loop through each item
    for Ii in I1,...In:
        
        # if the previous item fully depleted the budget, all remaining item counts are 0
        # and the function should return
        if U'[i - 1] == 0: 
            break

        P[i] = floor( U'[i-1] / ci )
        V[i] = V[i - 1] + P[i] * vi
        U'[i] = U'[i - 1] - P[i] * ci

    return P