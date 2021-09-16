from copy import deepcopy
from queue import Queue

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
        c_list[i] = {"b": b_list[i], "e": e_list[i], "p": i}

    # Return all children
    return [c_list[0], c_list[1], c_list[2], c_list[3]]


def BFS(fp):
    # Memorize visited states
    visited = []
    queue = Queue()
    # Put root to the queue
    queue.put({"b": fp.board, "e": fp.e_tile, "p": []})

    while True:
        # Solution is not found
        if queue.empty():
            return []

        # Get current node
        node = queue.get()

        # Found a solution
        if node["b"] == fp.goal:
            return node["p"]

        # Add current node to the visited list, and add its children to the queue
        if node["b"] not in visited:
            visited.append(node["b"])
            for child in children(fp, node["b"], node["e"]):
                if child["b"] not in visited:
                    queue.put(
                        {"b": child["b"], "e": child["e"], "p": node["p"] + [child["p"]]})
