import sys

FILENAME = sys.argv[1]
# FILENAME = "sample_input.txt"

file = open(FILENAME)

T = int(file.readline().strip())


def isWithinTenPercent(value, truth):
    if value > truth:
        return 0.9 * value <= truth
    elif value < truth:
        return 1.1 * value >= truth
    return True


def find_acceptable_ratios(ratio, truth, value):
    ans = []
    if isWithinTenPercent(ratio * truth, value):
        ans.append(ratio)

    pr = ratio + 1
    while True:
        if isWithinTenPercent(pr * truth, value):
            ans.append(pr)
            pr += 1
        else:
            break

    nr = ratio - 1
    while True:
        if isWithinTenPercent(nr * truth, value):
            ans.append(nr)
            nr -= 1
        else:
            break
    return ans


for i in range(T):
    line = file.readline().strip()
    N, P = map(int, line.split(' '))
    R = map(int, list(file.readline().strip().split(' ')))
    Q = [map(int, file.readline().strip().split(' ')) for _ in range(N)]

    ans = 0
    Qo = Q[0]
    for j, q in enumerate(Qo):
        elemMatch = False
        ratio = q / R[0]
        acceptable_ratios = find_acceptable_ratios(ratio, R[0], q)
        for ratio in acceptable_ratios:
            if elemMatch: break
            jj = []
            ratioMath = True
            for k, Qk in enumerate(Q[1:]):
                rowMatch = False
                l = 0
                for qt in Qk:
                    if isWithinTenPercent(ratio * R[k + 1], qt):
                        rowMatch = True
                        break
                    l += 1
                if rowMatch is False:
                    ratioMath = False
                    break
                else:
                    jj.append(l)
            if ratioMath:
                elemMatch = True
                ans += 1
                for k in range(len(Q) - 1):
                    Q[k + 1] = Q[k + 1][:jj[k]] + Q[k + 1][jj[k] + 1:]

    print "Case #" + str(i + 1) + ": " + str(ans)
