from copy import deepcopy
from test import test

from fifteen_puzzle import FP

# Start List-------------------------------------------------
start1 = [["1 ", "2 ", "3 ", "4 "], ["5 ", "6 ", "7 ", "8 "],
          ["9 ", "10", "11", "__"], ["13", "14", "15", "12"]]
start2 = [["1 ", "2 ", "3 ", "__"], ["5 ", "6 ", "7 ", "4 "],
          ["9 ", "10", "11", "8 "], ["13", "14", "15", "12"]]
start3 = [["1 ", "2 ", "7 ", "3 "], ["5 ", "6 ", "__", "4 "],
          ["9 ", "10", "11", "8 "], ["13", "14", "15", "12"]]
start4 = [["1 ", "2 ", "__", "3 "], ["5 ", "6 ", "7 ", "4 "],
          ["9 ", "10", "11", "8 "], ["13", "14", "15", "12"]]
start5 = [["6 ", "5 ", "2 ", "3 "], ["__", "1 ", "7 ", "4 "],
          ["9 ", "8 ", "10", "11"], ["13", "14", "15", "12"]]
start6 = [["1 ", "2 ", "3 ", "4 "], ["5 ", "6 ", "7 ", "8 "],
          ["__", "13", "12", "15"], ["14", "9 ", "11", "10"]]
start7 = [["5 ", "3 ", "9 ", "4 "], ["1 ", "__", "14", "11"],
          ["6 ", "2 ", "15", "8 "], ["13", "10", "7 ", "12"]]
start8 = [["6 ", "5 ", "13", "4 "], ["__", "2 ", "1 ", "3 "],
          ["14", "10", "8 ", "11"], ["7 ", "9 ", "15", "12"]]
start9 = [["9 ", "5 ", "4 ", "7 "], ["1 ", "10", "6 ", "2 "],
          ["13", "3 ", "11", "12"], ["__", "14", "8 ", "15"]]
start10 = [["5 ", "__", "10", "7 "], ["14", "4 ", "2 ", "3 "],
           ["8 ", "15", "1 ", "11"], ["6 ", "9 ", "13", "12"]]
# -----------------------------------------------------------


# Goal List--------------------------------------------------
# goal4 is assigned to the pair with start 1, 2, 3, and 4
goal4 = [["1 ", "2 ", "3 ", "4 "], ["5 ", "6 ", "7 ", "8 "],
         ["9 ", "10", "11", "12"], ["13", "14", "15", "__"]]
goal5 = [["6 ", "5 ", "2 ", "3 "], ["8 ", "9 ", "7 ", "4 "],
         ["__", "1 ", "10", "11"], ["13", "14", "15", "12"]]
goal6 = [["2 ", "3 ", "7 ", "4 "], ["1 ", "6 ", "8 ", "15"],
         ["5 ", "13", "12", "__"], ["14", "9 ", "11", "10"]]
goal7 = [["5 ", "9 ", "4 ", "11"], ["1 ", "3 ", "14", "__"],
         ["6 ", "2 ", "15", "8 "], ["13", "10", "7 ", "12"]]
goal8 = [["6 ", "5 ", "13", "4 "], ["10", "1 ", "__", "3 "],
         ["2 ", "14", "8 ", "11"], ["7 ", "9 ", "15", "12"]]
goal9 = [["9 ", "5 ", "4 ", "7 "], ["1 ", "__", "10", "6 "],
         ["3 ", "11", "12", "2 "], ["13", "14", "8 ", "15"]]
goal10 = [["5 ", "4 ", "10", "7 "], ["14", "2 ", "1 ", "3 "],
          ["8 ", "15", "13", "11"], ["6 ", "9 ", "__", "12"]]
# -----------------------------------------------------------


def get_shuffled_pair(st_shfl=20, gl_shfl=20):
    # st_shfl - shuffle power for the start
    # gl_shfl - shuffle power for the goal
    # return start, goal
    fp = FP()
    fp2 = FP()

    fp.shuffle_puzzle(st_shfl)

    start_fp2 = deepcopy(fp.board)
    fp2.set_start(start_fp2)
    fp2.shuffle_puzzle(gl_shfl)
    fp.set_goal(fp2.board)

    print("start:", fp.board)
    print("goal:", fp.goal)

    return fp.board, fp.goal


def main():
    # Append every pair into pairs list and then pass it into the test function
    pairs = []
    pairs.append({"start": start1, "goal": goal4})
    pairs.append({"start": start2, "goal": goal4})
    pairs.append({"start": start3, "goal": goal4})
    pairs.append({"start": start4, "goal": goal4})
    pairs.append({"start": start5, "goal": goal5})
    pairs.append({"start": start6, "goal": goal6})
    pairs.append({"start": start7, "goal": goal7})
    pairs.append({"start": start8, "goal": goal8})
    pairs.append({"start": start9, "goal": goal9})
    pairs.append({"start": start10, "goal": goal10})

    print("---Test Started---")
    test(pairs)
    print("----Test Ended----")

    # start, goal = get_shuffled_pair(300, 10)
    # print(start)
    # print(goal)

    return


if __name__ == "__main__":
    main()
