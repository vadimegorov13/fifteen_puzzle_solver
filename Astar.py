from copy import deepcopy
from math import floor

from fifteen_puzzle import MAX_INDEX

# Citation: https://brilliant.org/wiki/a-star-search/


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
        c_list[i] = {"b": b_list[i], "e": e_list[i], "p": i, "g": 0, "h": get_h(b_list[i])}

    # Return all children
    return [c_list[0], c_list[1], c_list[2], c_list[3]]

# Get h score
def get_h(board):
    h = 0
    for i in range(MAX_INDEX):
        for j in range(MAX_INDEX):
            if board[i][j] != "__":
                tile_check = int(board[i][j])
                goal_x = floor((tile_check - 1) / MAX_INDEX)
                goal_y = floor((tile_check - 1) % MAX_INDEX)
                dx = i - goal_x
                dy = j - goal_y
                h += abs(dx) + abs(dy)
    return h

# Pop the node with the lowest f score in the open list
def min_f(open):
    index, index_of_min = 0, 0
    min = 100

    for node in open:
        f = node["g"] + node["h"]

        if f < min:
            min = f
            index_of_min = index
        index += 1

    return open.pop(index_of_min)

def AStar(fp):
    # Create open and closed list
    open = []
    closed = []
    # Put root to the open list
    root = {"b": fp.board, "e": fp.e_tile, "p": [], "g": 0, "h": get_h(fp.board)}
    open.append(root)

    while True:
        # Pop the node with the lowest f score in the open list
        node = min_f(open)

        # Solution found
        if node["b"] == fp.goal:
            return node["p"]

        # If solution is not found put the node in the closed list
        closed.append(node)

        # Look at each child of the current node
        for child in children(fp, node["b"], node["e"]):
            if child["g"] < node["g"] and child in closed:
                # Replace the child with the new, lower, g value
                # Current node is now the child's parent
                node, child = child, node
            elif node["g"] < child["g"] and child in open:
                # Replace the child with the new, lower, g value
                # Change the child's parent to our current node
                node, child = child, node
            elif child not in closed and child not in open:
                # Append current node into an open list
                open.append({"b": child["b"], "e": child["e"], "p": node["p"] + [child["p"]], "g": node["g"] + 1, "h": child["h"]})
