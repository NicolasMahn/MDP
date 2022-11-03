import numpy as np
import math

gamma = 0.9
minGamma = 0.1

statecolumns = 3
staterows = 3

rewards = np.matrix([[0, 0, 40],
                     [0, -50, -np.inf],
                     [0, 0, 10]])


def getVandPi(s, rec_depth=0):
    v = -np.inf
    pi = ""
    if rec_depth > 10:
        return 0, ""
    if math.pow(gamma, rec_depth) < minGamma:
        v1 = 0
    # print(rec_depth, math.pow(gamma, rec_depth))
    if s[0]-1 >= 0 and not (s[0]-1 == 1 and s[1] == 2):
        if math.pow(gamma, rec_depth) >= minGamma:
            v1,_ = getVandPi((s[0] - 1, s[1]), rec_depth + 1)
        res = rewards.item(s[0]-1, s[1]) + gamma * v1
        if res > v:
            v = res
            pi = "N"
    if s[0]+1 < staterows and not (s[0]+1 == 1 and s[1] == 2):
        if math.pow(gamma, rec_depth) >= minGamma:
            v1,_ = getVandPi((s[0] + 1, s[1]), rec_depth + 1)
        res = rewards.item(s[0]+1, s[1]) + gamma * v1
        if res > v:
            v = res
            pi = "S"
        elif res == v:
            pi += " & S"

    if s[1]-1 >= 0 and not (s[0] == 1 and s[1]-1 == 2):
        if math.pow(gamma, rec_depth) >= minGamma:
            v1,_ = getVandPi((s[0], s[1] - 1), rec_depth + 1)
        res = rewards.item(s[0], s[1]-1) + gamma * v1
        if res > v:
            v = res
            pi = "W"
        elif res == v:
            pi += " & W"
    if s[1]+1 < statecolumns and not (s[0] == 1 and s[1]+1 == 2):
        if math.pow(gamma, rec_depth) >= minGamma:
            v1,_ = getVandPi((s[0], s[1] + 1), rec_depth + 1)
        res = rewards.item(s[0], s[1]+1) + gamma * v1
        if res > v:
            v = res
            pi = "E"
        elif res == v:
            pi += " & E"

    if s[0]-1 >= 0 and s[1]-1 >= 0 and not (s[0]-1 == 1 and s[1]-1 == 2):
        if math.pow(gamma, rec_depth) >= minGamma:
            v1,_ = getVandPi((s[0] - 1, s[1] - 1), rec_depth + 1)
        res = rewards.item(s[0]-1, s[1]-1) + gamma * v1
        if res > v:
            v = res
            pi = "NW"
        elif res == v:
            pi += " & NW"
    if s[0]+1 < staterows and s[1]+1 <statecolumns and not (s[0]+1 == 1 and s[1]+1 == 2):
        if math.pow(gamma, rec_depth) >= minGamma:
            v1,_ = getVandPi((s[0] + 1, s[1] + 1), rec_depth + 1)
        res = rewards.item(s[0]+1, s[1]+1) + gamma * v1
        if res > v:
            v = res
            pi = "SE"
        elif res == v:
            pi += " & SE"

    if s[0]-1 >= 0 and s[1]+1 < statecolumns and not (s[0]-1 == 1 and s[1]+1 == 2):
        if math.pow(gamma, rec_depth) >= minGamma:
            v1,_ = getVandPi((s[0] - 1, s[1] + 1), rec_depth + 1)
        res = rewards.item(s[0]-1, s[1]+1) + gamma * v1
        if res > v:
            v = res
            pi = "NE"
        elif res == v:
            pi += " & NE"
    if s[0]+1 <staterows and s[1]-1 >= 0 and not (s[0]+1 == 1 and s[1]-1 == 2):
        if math.pow(gamma, rec_depth) >= minGamma:
            v1,_ = getVandPi((s[0] + 1, s[1] - 1), rec_depth + 1)
        res = rewards.item(s[0]+1, s[1]-1) + gamma * v1
        if res > v:
            v = res
            pi = "SW"
        elif res == v:
            pi += " & SW"

    return v, pi


def main():

    for r in range(0, staterows):
        for c in range(0, statecolumns):

            s = (r,c)
            v, pi =getVandPi(s)

            print(f"State: {chr(97 + s[1])}{3 - s[0]} ")
            print(f"    Pi*: {pi}")
            print(f"    V*(s): {v}")
            print()


if __name__ == '__main__':
    main()


