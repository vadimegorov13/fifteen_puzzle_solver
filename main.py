from fifteen_puzzle import FP
from BFS import BFS

test = [["1 ", "2 ", "3 ", "4 "], ["5 ", "6 ", "7 ", "__"],
         ["9 ", "10", "11", "8 "], ["13", "14", "15", "12"]]

def main():
    fp = FP()

    fp.shuffle_puzzle()
    print("Shuffled board:")
    fp.display()
    
    print("Solving the puzzle...")
    path = BFS(fp)
    print(path)
    for p in path:
        fp.shifts[p](fp.board, fp.e_tile)
        fp.display()


if __name__ == "__main__":
    main()
