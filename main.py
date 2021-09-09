from fifteen_puzzle import FP

test = [["1 ", "2 ", "3 ", "4 "], ["5 ", "6 ", "7 ", "__"],
         ["9 ", "10", "11", "8 "], ["13", "14", "15", "12"]]

def main():
    fp = FP()

    fp.set_start(test) 
    fp.display()

    fp.shuffle_puzzle()
    print("Shuffled board:")
    fp.display()


if __name__ == "__main__":
    main()
