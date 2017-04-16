import sys

# FILENAME = sys.argv[1]
FILENAME = "sample_input.txt"

file = open(FILENAME)

T = int(file.readline().strip())

for i in range(T):
    line = file.readline().strip()
    Hd, Ad, Hk, Ak, B, D = map(int, line.split(' '))

