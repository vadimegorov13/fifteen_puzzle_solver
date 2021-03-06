from copy import deepcopy
from test import test

from fifteen_puzzle import FP

# Start List-------------------------------------------------
start1 = [["1 ", "2 ", "3 ", "4 "], ["5 ", "6 ", "7 ", "8 "],
          ["9 ", "10", "11", "__"], ["13", "14", "15", "12"]]
start2 = [["3 ", "5 ", "2 ", "4 "], ["__", "9 ", "10", "8 "],
          ["13", "7 ", "1 ", "15"], ["14", "6 ", "11", "12"]]
start3 = [["7 ", "11", "2 ", "6 "], ["1 ", "10", "12", "4 "],
          ["14", "5 ", "8 ", "15"], ["13", "9 ", "__", "3 "]]
start4 = [["6 ", "9 ", "2 ", "4 "], ["__", "1 ", "12", "3 "],
          ["5 ", "10", "7 ", "14"], ["11", "15", "13", "8 "]]
start5 = [["1 ", "9 ", "10", "3 "], ["13", "14", "2 ", "4 "],
          ["7 ", "__", "11", "8 "], ["15", "5 ", "6 ", "12"]]
start6 = [["6 ", "4 ", "5 ", "8 "], ["1 ", "11", "14", "10"],
          ["9 ", "13", "12", "2 "], ["7 ", "3 ", "__", "15"]]
start7 = [["13", "7 ", "1 ", "4 "], ["2 ", "15", "6 ", "11"],
          ["3 ", "8 ", "9 ", "14"], ["5 ", "12", "10", "__"]]
start8 = [["10", "__", "13", "4 "], ["7 ", "2 ", "6 ", "8 "],
          ["1 ", "3 ", "12", "11"], ["9 ", "5 ", "14", "15"]]
start9 = [["2 ", "__", "8 ", "7 "], ["1 ", "6 ", "3 ", "4 "],
          ["5 ", "13", "11", "12"], ["10", "9 ", "15", "14"]]
start10 = [["1 ", "7 ", "5 ", "4 "], ["14", "3 ", "12", "6 "],
           ["9 ", "2 ", "11", "15"], ["13", "8 ", "__", "10"]]
# -----------------------------------------------------------


# Goal List--------------------------------------------------
goal1 = [["1 ", "2 ", "3 ", "4 "], ["5 ", "6 ", "7 ", "8 "],
         ["9 ", "10", "11", "12"], ["13", "14", "15", "__"]]
goal2 = [["3 ", "5 ", "2 ", "4 "], ["13", "9 ", "10", "8 "],
         ["7 ", "__", "1 ", "15"], ["14", "6 ", "11", "12"]]
goal3 = [["7 ", "11", "2 ", "6 "], ["1 ", "10", "12", "__"],
         ["14", "5 ", "8 ", "4 "], ["13", "9 ", "3 ", "15"]]
goal4 = [["6 ", "9 ", "2 ", "4 "], ["1 ", "__", "7 ", "3 "],
         ["5 ", "12", "10", "14"], ["11", "15", "13", "8 "]]
goal5 = [["1 ", "9 ", "10", "3 "], ["13", "2 ", "4 ", "8 "],
         ["7 ", "__", "14", "11"], ["15", "5 ", "6 ", "12"]]
goal6 = [["6 ", "4 ", "5 ", "8 "], ["1 ", "__", "11", "10"],
         ["13", "12", "14", "2 "], ["9 ", "7 ", "3 ", "15"]]
goal7 = [["13", "7 ", "1 ", "4 "], ["3 ", "2 ", "9 ", "6 "],
         ["__", "15", "8 ", "11"], ["5 ", "12", "10", "14"]]
goal8 = [["10", "2 ", "13", "4 "], ["7 ", "3 ", "__", "8 "],
         ["1 ", "14", "6 ", "11"], ["9 ", "12", "5 ", "15"]]
goal9 = [["2 ", "6 ", "8 ", "__"], ["5 ", "1 ", "3 ", "7 "],
         ["13", "11", "12", "4 "], ["10", "9 ", "15", "14"]]
goal10 = [["1 ", "7 ", "5 ", "4 "], ["14", "12", "6 ", "15"],
          ["2 ", "3 ", "__", "11"], ["9 ", "13", "8 ", "10"]]
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

    return fp.board, fp.goal


def main():
    # Append every pair into pairs list and then pass it into the test function
    pairs = []
    pairs.append({"start": start1, "goal": goal1})
    pairs.append({"start": start2, "goal": goal2})
    pairs.append({"start": start3, "goal": goal3})
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

    # start, goal = get_shuffled_pair(300, 20)
    # print("start:", start)
    # print("goal:", goal)

    return


if __name__ == "__main__":
    main()
