def bus_stops(BR1...BRn, curr, m):

    # there may not be a valid path from every point i to m,
    # so fill all spots except the ending 
    cost = [ infinity ]
    cost[m] = 0

    for k from m - 1 to 1:
        for all BRi in BR1...BRn such that si <= k < fi:
            cost[k] = min(cost[k], ci + cost[fi])
    
    return cost[1]