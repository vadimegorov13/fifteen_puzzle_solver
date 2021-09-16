from copy import deepcopy
from os import system
from time import perf_counter

from AStar import AStar
from BFS import BFS
from fifteen_puzzle import FP
from GBFS import GBFS


def cool_table_print(list_to_print):
    pair_num = 0
    pair_num_str = ""

    system("clear")  # You can remove this line if you want
    print("{:<10} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
        'Pair #', '| Algorithm', '| Time(s)', '| Nodes exp.', '| Path length', '| Path'))

    print("{:<10} {:<15} {:<15} {:<15} {:<15} {:<15}\n".format(
        '#', '| name', '| seconds', '| #', '| #', '| 0: up, 1: down, 2: left, 3: right'))

    for l in list_to_print:
        if l["a"] == "BFS":
            pair_num += 1
            pair_num_str = str(pair_num)
        else:
            pair_num_str = ""

        print("{:<10} {:<15} {:<15} {:<15} {:<15} {:<15}".format(pair_num_str,
              "| " + l["a"], "| " + str(round(l["t"], 10)), "| " + str(l["np"]), "| " + str(len(l["p"])), "| " + str(l["p"])))


def test(pairs):
    fp = FP()
    algorithms = [BFS, GBFS, AStar]
    list_to_print = []

    for pair in pairs:
        for algorithm in algorithms:
            fp.set_start(deepcopy(pair["start"]))
            fp.set_goal(deepcopy(pair["goal"]))

            start_t = perf_counter()
            path, opened_nodes = algorithm(fp)
            stop_t = perf_counter()

            list_to_print.append({"a": algorithm.__name__, "t": stop_t - start_t, "p": path, "np": opened_nodes})
            cool_table_print(list_to_print)
