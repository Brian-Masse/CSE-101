
# pass in the list of pairs, the size of the list, and half the total weight
# The final piece can be precomputed in linear time. 
weighted_median(list L, size n, WM):

    # Find the median of the given list (by value, not weight)
    # Using the select algorithm from class
    median = select_lowest(L, n / 2)

    # create 3 sub array for pairs with a value <, =, > the median
    # keep track of their cumulative weight
    SL = []; WL = 0;
    SM = []
    SR = []; WR = 0;

    # loop through the list to build sub arrays.
    for pair in L:
        if pair.value < median.value:
            SL.add(pair)
            WL += pair.weight
        elif pair.value > median.value:
            SR.add(pair)
            WR += pair.weight
        else:
            SM.add(pair)

    # if both sides are less than the target weight, that value is the weighted median
    if (WL < WM && WR < WM):
        return median

    # run the algorithm recursively on whichever subset was greater than the target weight
    if (WL > WM):
        return weighted_median(WL, WL.size(), WM)
    else:
        return weighted_median(WR, WR.size(), WM)