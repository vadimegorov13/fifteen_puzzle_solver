from copy import deepcopy
from math import floor

from fifteen_puzzle import MAX_INDEX


def children(fp, board, e_tile):
    # Populate board list, empty tile location list, and children list
    b_list, e_list, c_list = [None] * \
        MAX_INDEX, [None] * MAX_INDEX, [None] * MAX_INDEX

    for i in range(MAX_INDEX):
        # Copy b and e into b_list and e_list
        b_list[i] = deepcopy(board)
        e_list[i] = deepcopy(e_tile)
        # Shift tile; Assign board, empty tile, and shift direction to the child
        b_list[i], e_list[i] = fp.shifts[i](b_list[i], e_list[i])
        c_list[i] = {"b": b_list[i], "e": e_list[i], "p": i, "h": mdh(b_list[i], fp.goal)}

    # Return all children
    return [c_list[0], c_list[1], c_list[2], c_list[3]]

def mdh(b, g):
    total_dist = 0
    for x1 in range(MAX_INDEX):
        for y1 in range(MAX_INDEX):
            for x2 in range(MAX_INDEX):
                for y2 in range(MAX_INDEX):
                    if b[x1][y1] == g[x2][y2]:
                        total_dist += abs(x1 - x2) + abs(y1 - y2)
    return total_dist


def min_h(queue):
    index, index_of_min = 0, 0
    min = 9999
    for node in queue:
        if node["h"] < min:
            min = node["h"]
            index_of_min = index
        index += 1
    return queue.pop(index_of_min)


def GBFS(fp):
    visited = []
    queue = []
    opened_nodes = 0

    queue.append({"b": fp.board, "e": fp.e_tile, "p": [], "h": mdh(fp.board, fp.goal)})

    while True:

        node = min_h(queue)

        if node["b"] == fp.goal:
            return node["p"], opened_nodes + 1
    
        visited.append(node)

        for child in children(fp, node["b"], node["e"]):
            if child["h"] < node["h"] and child in visited:
                node, child = child, node
            elif node["h"] < node["h"] and child in queue:
                node, child = child, node
            elif child not in queue and child not in visited:
                opened_nodes += 1
                queue.append({"b": child["b"], "e": child["e"], "p": node["p"] + [child["p"]], "h": child["h"]})
