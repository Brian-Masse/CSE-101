import random
import numpy as np
from typing import Tuple

# MARK: construct_graph
def construct_graph(size: int):

    graph = np.zeros((size, size))

    # simulate generating 5|V| random edges
    prob = (5 * size) / pow(size, 2)

    for row in range(0, size):
        for col in range(0, size):
            edge_weight = random.random()

            edge = 1 if edge_weight < prob else 0
            graph[row][col] = edge
    
    return graph

# MARK: heuristic_coloring
def heuristic_coloring(size: int):

    graph = construct_graph(size=size)
    edge_colors: dict[int, int] = dict()
    ordered_edges: list[Tuple[int, int]] = []

    # sort edges by neighbors
    for i in range(0, size):
        neighbors = int(sum(graph[:, i]))

        edge = (i, neighbors)

        if i == 0:
            ordered_edges.append(edge)
            continue

        f = 0
        while f < len(ordered_edges) and (ordered_edges[f][1] > edge[1]):
            f += 1
        ordered_edges.insert(f, edge)

    # Assign colors
    for i in range(0, size):
        neighbors = graph[:, i]

        proposed_color = 1
        for j in range(0, size):
            if neighbors[j] == 1 and edge_colors.get(j) == proposed_color:
                proposed_color += 1

        edge_colors[i] = proposed_color

    return max(edge_colors.values())


def run_experiment():

    graph_count = 15

    for i in range(3, 12):

        size = pow(2, i)
        sum = 0
        individual: list[int] = []
        print("Running for |V| = ", size)

        for _ in range(0, graph_count):
            result = heuristic_coloring(size=size)
            sum += result
            individual.append(result)
            # print(f"{j}: {result}")

        avg = sum / graph_count

        print(f"avg: {avg}, {individual}")
        print("-----------")


def main():
    run_experiment()

if __name__ == "__main__":
    main()