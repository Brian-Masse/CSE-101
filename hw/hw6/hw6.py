
# pass in the list of pairs, the size of the list, and half the total weight
# The final piece can be precomputed in linear time. 
def weighted_median(list L, size n, WM):

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



# pass in a node to start on. In the specialized problem, this will always be the root. 
# The function returns 2 things:
#   1. The highest weight independent set with the root
#   2. The highest weight independent set without the root
# The answer is the set with the larger weight at the end. 
def WeightedSets(node):

    if node has no children:
        return ( [node], [] )

    if node has 1 child:
        return ( [node], [child] )
    
    left_result = WeightedSets(leftChild)
    right_result = WeightedSets(rightChild)

    with_left = left_result[0]; without_left = left_result[1]
    with_right = right_result[0]; without_right = right_result[1]

    with_node = [], without_node = []

    # Generate the optimal set containing the current node
    with_node += without_left + without_right + node

    # generate the optimal set without the current node
    if weight(with_right) > weight(without_right):
        without_node += with_right
    else:
        without_node += without_right
    if weight(with_left) > weight(without_left):
        without_node += with_left
    else:
        without_node += without_left
    
    return with_node, without_node