from queue import Queue
from copy import deepcopy


def successors(fp, b, e):
    b_list = [deepcopy(b), deepcopy(b), deepcopy(b), deepcopy(b)]
    e_list = [deepcopy(e), deepcopy(e), deepcopy(e), deepcopy(e)]

    b_list[0], e_list[0] = fp.shift_up(b_list[0], e_list[0])
    b_list[1], e_list[1] = fp.shift_down(b_list[1], e_list[1])
    b_list[2], e_list[2] = fp.shift_left(b_list[2], e_list[2])
    b_list[3], e_list[3] = fp.shift_right(b_list[3], e_list[3])

    return [[b_list[0], e_list[0], 0], [b_list[1], e_list[1], 1], [b_list[2], e_list[2], 2], [b_list[3], e_list[3], 3]]


def BFS(fp):
    visited = []
    queue = Queue()
    queue.put({"b": fp.board, "e": fp.e_tile, "p": []})

    while True:
        if queue.empty():
            return []

        node = queue.get()

        # found a solution
        if node["b"] == fp.goal:
            return node["p"]

        if node["b"] not in visited:
            visited.append(node["b"])
            for child in successors(fp, node["b"], node["e"]):
                if child[0] not in visited:
                    queue.put(
                        {"b": child[0], "e": child[1], "p": node["p"] + [child[2]]})

