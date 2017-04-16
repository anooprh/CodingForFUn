import sys

FILENAME = sys.argv[1]
# FILENAME = "sample_input.txt"

file = open(FILENAME)

T = int(file.readline().strip())

for i in range(T):
    line = file.readline().strip().lstrip('0')
    l, n = list(line), len(line)
    last_zero = n
    for j in range(n - 1, 0, -1):
        if ord(l[j]) < ord(l[j - 1]):
            l[j - 1] = chr(ord('0') + (ord(l[j - 1]) - ord('0') - 1) % 10)
            last_zero = j
    for j in range(last_zero, n):
        l[j] = '9'
    print "Case #" + str(i + 1) + ": " + ''.join(l).lstrip('0')
