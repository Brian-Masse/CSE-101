import heapq
import math
import random

# MARK: generate_adjacency_list
def generate_adjacency_list(size: int) -> list[list[tuple[int, int]]]:
    adjacencyList: list[list[tuple[int, int]]] = []

    for i in range(0, size):
        edges: list[tuple[int, int]] = []

        # generate a random list of edges from i to j
        for j in range(0, size):
            if j != i:
                edge_weight = random.random()
                edge = (edge_weight, j)
                edges.append(edge)

        adjacencyList.append(edges)

    print(f"Finished Generating Complete Graph with {size} verticies")
    return adjacencyList


# MARK: djikstras
# adjacencyList stores a list of tuples (weight, label)
def djikstras(adjacencyList: list[list[tuple[int, int]]] ) -> int:

    vertex_count = len(adjacencyList)

    # Initialize the frontier with the first node (labeled 0) distance 0
    # And remaining verticies distance infinity
    # frontier is stored as (distance, label)
    frontier: list[tuple[int, int]] = [(0, 0)]
    explored: list[tuple[int, int]] = []

    count = 0

    for i in range(1, vertex_count):
        frontier.append( (math.inf, i) )

    heapq.heapify(frontier)

    while (len(frontier) != 0):
        current_vertex = heapq.heappop(frontier)
        heap_size = len(frontier)

        for edge in adjacencyList[current_vertex[1]]:
            label = edge[1]

            # find the label in the heap
            vertex_indicies = [i for i in range(0, heap_size) if frontier[i][1] == label]
            if len(vertex_indicies) > 0:
                vertex_index = vertex_indicies[0]

                vertex_distance = frontier[vertex_index][0]
                current_distance = current_vertex[0]
                edge_length = edge[0]

                # update the distance of that vertex
                if vertex_distance > current_distance + edge_length:
                    frontier[vertex_index] = (current_distance + edge_length, label)
                    heapq.heapify(frontier)
                    count += 1
    
        explored.append(current_vertex)
    
    return count

def main():
    data: list[tuple[int, int]] = []

    for i in range(0, 12):
        vertex_count = pow(2, i)
        verticies = generate_adjacency_list(size=vertex_count)

        count = djikstras(adjacencyList=verticies)
        print(f"Completed Djikstras with {vertex_count} verticies. Called decrease-key {count} times!", "\n")

        data.append( (vertex_count, count))

    print(data)

if __name__ == "__main__":
    main()