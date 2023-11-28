#!/usr/bin/python3
for i in range(ord('z'), ord('a') - 1, -1):
    if i % 2 == 0:
        remove = 0
    else:
        remove = 32
    print('{}'.format(chr(i - remove)), end='')
