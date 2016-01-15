#!/usr/bin/env python

import piglow
from time import sleep

piglow.auto_update = True

tmp_arr = []

for count in range(4):
    for x in reversed(range(6)):
        arr = [x, x + 6, x + 12]
        piglow.set(arr, 20)
        sleep(0.05)
        if len(tmp_arr) > 0:
            piglow.set(tmp_arr, 0)
            sleep(0.03)
        tmp_arr = arr
