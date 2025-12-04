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
