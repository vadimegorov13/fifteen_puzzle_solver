from fifteen_puzzle import FP
from AStar import AStar
from BFS import BFS
from os import system
from time import sleep

test = [["1 ", "2 ", "3 ", "4 "],
        ["5 ", "6 ", "7 ", "__"],
        ["9 ", "10", "11", "8 "],
        ["13", "14", "15", "12"]]

# [2, 0, 3, 1, 3, 3]
test2 = [["1 ", "2 ", "3 ", "4 "],
        ["5 ", "6 ", "7 ", "8 "],
        ["13", "9 ", "11", "12"],
        ["10", "__", "14", "15"]]

test3 = [["2 ", "3 ", "4 ", "8 "],
        ["1 ", "5 ", "10", "12"],
        ["9 ", "7 ", "6 ", "__"],
        ["13", "14", "11", "15"]]

# It's not really that cool, just shows a step by step solution
def cool_display(fp, path):
    for p in path:
        # system("clear") # You can remove this line if you want
        # print("Solution")
        # print("Path: ", path)
        fp.shifts[p](fp.board, fp.e_tile)
        fp.display()
        sleep(1)


def main():
    # Initialize fifteen puzzle
    fp = FP()

    # Shuffle the puzzle
    # fp.shuffle_puzzle()
    fp.set_start(test2)
    print("Shuffled board:\n")
    fp.display()
    sleep(2) # Wait 2 seconds

    # Solve it with BFS
    print("Solving the puzzle...")
    # path = BFS(fp)
    path = AStar(fp)
    print(path)
    cool_display(fp, path)


if __name__ == "__main__":
    main()
