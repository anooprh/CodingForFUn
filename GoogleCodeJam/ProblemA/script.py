import sys

FILENAME = sys.argv[1]
# FILENAME = "sample_input.txt"

file = open(FILENAME)

T = int(file.readline().strip())

for i in range(T):
    line = file.readline().strip()
    # line = "+++--+--- 3"
    arr = [True if c == '+' else False for c in list(line.split(' ')[0])]
    width = int(line.split(' ')[1])
    n = len(arr)
    ans = 0
    b = False
    for j in range(n - width):
        if arr[j] is False:
            ans += 1
            for k in range(width):
                arr[j + k] = not arr[j + k]
    prev = arr[n - width]
    for j in range(n - width + 1, n):
        if arr[j] is not prev:
            print "Case #" + str(i + 1) + ": IMPOSSIBLE"
            b = True
            break
    if b: continue
    if not prev:
        ans += 1
    print "Case #" + str(i + 1) + ": " + str(ans)
