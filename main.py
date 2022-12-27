import numpy as np
import math

gamma = 0.9
min_gamma = 0.1

state_columns = 3
state_rows = 3

rewards = np.matrix([[0, 0, 40],
                     [0, -50, -np.inf],
                     [0, 0, 10]])


def get_v_and_pi(s, rec_depth=0, cumulative=False, max_rec_depth=9):
    if cumulative:
        v = 0
    else:
        v = -np.inf
    pi = ""
    if rec_depth > max_rec_depth:
        return 0, ""
    if math.pow(gamma, rec_depth) < min_gamma:
        v1 = 0

    possible_actions = 0

    if s[0]-1 >= 0 and not (s[0]-1 == 1 and s[1] == 2):
        if math.pow(gamma, rec_depth) >= min_gamma:
            v1,_ = get_v_and_pi((s[0] - 1, s[1]), rec_depth + 1, cumulative, max_rec_depth)
        res = rewards.item(s[0]-1, s[1]) + gamma * v1
        if cumulative:
            v += res
            possible_actions += 1
        else:
            if res > v:
                v = res
                pi = "N"
    if s[0]+1 < state_rows and not (s[0] + 1 == 1 and s[1] == 2):
        if math.pow(gamma, rec_depth) >= min_gamma:
            v1,_ = get_v_and_pi((s[0] + 1, s[1]), rec_depth + 1, cumulative, max_rec_depth)
        res = rewards.item(s[0]+1, s[1]) + gamma * v1
        if cumulative:
            v += res
            possible_actions += 1
        else:
            if res > v:
                v = res
                pi = "S"
            elif res == v:
                pi += " & S"

    if s[1]-1 >= 0 and not (s[0] == 1 and s[1]-1 == 2):
        if math.pow(gamma, rec_depth) >= min_gamma:
            v1,_ = get_v_and_pi((s[0], s[1] - 1), rec_depth + 1, cumulative, max_rec_depth)
        res = rewards.item(s[0], s[1]-1) + gamma * v1
        if cumulative:
            v += res
            possible_actions += 1
        else:
            if res > v:
                v = res
                pi = "W"
            elif res == v:
                pi += " & W"
    if s[1]+1 < state_columns and not (s[0] == 1 and s[1] + 1 == 2):
        if math.pow(gamma, rec_depth) >= min_gamma:
            v1,_ = get_v_and_pi((s[0], s[1] + 1), rec_depth + 1, cumulative, max_rec_depth)
        res = rewards.item(s[0], s[1]+1) + gamma * v1
        if cumulative:
            v += res
            possible_actions += 1
        else:
            if res > v:
                v = res
                pi = "E"
            elif res == v:
                pi += " & E"

    if s[0]-1 >= 0 and s[1]-1 >= 0 and not (s[0]-1 == 1 and s[1]-1 == 2):
        if math.pow(gamma, rec_depth) >= min_gamma:
            v1,_ = get_v_and_pi((s[0] - 1, s[1] - 1), rec_depth + 1, cumulative, max_rec_depth)
        res = rewards.item(s[0]-1, s[1]-1) + gamma * v1
        if cumulative:
            v += res
            possible_actions += 1
        else:
            if res > v:
                v = res
                pi = "NW"
            elif res == v:
                pi += " & NW"
    if s[0]+1 < state_rows and s[1]+1 < state_columns and not (s[0] + 1 == 1 and s[1] + 1 == 2):
        if math.pow(gamma, rec_depth) >= min_gamma:
            v1,_ = get_v_and_pi((s[0] + 1, s[1] + 1), rec_depth + 1, cumulative, max_rec_depth)
        res = rewards.item(s[0]+1, s[1]+1) + gamma * v1
        if cumulative:
            v += res
            possible_actions += 1
        else:
            if res > v:
                v = res
                pi = "SE"
            elif res == v:
                pi += " & SE"

    if s[0]-1 >= 0 and s[1]+1 < state_columns and not (s[0] - 1 == 1 and s[1] + 1 == 2):
        if math.pow(gamma, rec_depth) >= min_gamma:
            v1,_ = get_v_and_pi((s[0] - 1, s[1] + 1), rec_depth + 1, cumulative, max_rec_depth)
        res = rewards.item(s[0]-1, s[1]+1) + gamma * v1
        if cumulative:
            v += res
            possible_actions += 1
        else:
            if res > v:
                v = res
                pi = "NE"
            elif res == v:
                pi += " & NE"
    if s[0]+1 < state_rows and s[1]-1 >= 0 and not (s[0] + 1 == 1 and s[1] - 1 == 2):
        if math.pow(gamma, rec_depth) >= min_gamma:
            v1,_ = get_v_and_pi((s[0] + 1, s[1] - 1), rec_depth + 1, cumulative, max_rec_depth)
        res = rewards.item(s[0]+1, s[1]-1) + gamma * v1
        if cumulative:
            v += res
            possible_actions += 1
        else:
            if res > v:
                v = res
                pi = "SW"
            elif res == v:
                pi += " & SW"

    if cumulative:
        v = v/possible_actions

    return v, pi


def main():

    print("What would Information would you like?")
    print("1. The value state calculations from the MRP section")
    print("2. The optimal value state and policy in figure 11")

    num = input("please input the number of the wanted result \n")
    print("\n")

    if num == "1":
        for r in range(0, state_rows):
            for c in range(0, state_columns):
                s = (r,c)
                v, pi = get_v_and_pi(s, cumulative=True, max_rec_depth=2)

                print(f"State: {chr(97 + s[1])}{3 - s[0]} ")
                print(f"    v(s): {v}")
                print()
    else:
        for r in range(0, state_rows):
            for c in range(0, state_columns):
                s = (r, c)
                v, pi = get_v_and_pi(s)

                print(f"State: {chr(97 + s[1])}{3 - s[0]} ")
                print(f"    pi*: {pi}")
                print(f"    v*(s): {v}")
                print()


if __name__ == '__main__':
    main()


