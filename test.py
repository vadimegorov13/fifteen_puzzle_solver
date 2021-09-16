from fifteen_puzzle import FP
from AStar import AStar
from BFS import BFS
from GBFS import GBFS
from time import perf_counter
from copy import deepcopy
from os import system


def puzzle_is_solved(fp, path):
    for p in path:
        fp.shifts[p](fp.board, fp.e_tile)

    if fp.board == fp.goal:
        return True
    return False


def cool_table_print(list_to_print):
    pair_num = 0
    pair_num_str = ""

    system("clear") # You can remove this line if you want
    print("{:<10} {:<15} {:<15} {:<15}\n".format(
        'Pair', 'Algorithm', 'Time', 'Path'))

    for l in list_to_print:
        if l["a"] == "BFS":
            pair_num += 1
            pair_num_str = str(pair_num)
        else:
            pair_num_str = ""

        print("{:<10} {:<15} {:<15} {:<15}".format(pair_num_str, l["a"], str(round(l["t"], 10)), str(l["p"])))
       

def test(pairs):
    fp = FP()
    algorithms = [BFS, GBFS, AStar]
    list_to_print = []

    for pair in pairs:
        for algorithm in algorithms:
            fp.set_start(deepcopy(pair["start"]))
            fp.set_goal(deepcopy(pair["goal"]))

            start_t = perf_counter()
            path = algorithm(fp)
            stop_t = perf_counter()

            if puzzle_is_solved(fp, path):
                list_to_print.append(
                    {"a": algorithm.__name__, "t": stop_t - start_t, "p": path})
            cool_table_print(list_to_print)

