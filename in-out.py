#!/usr/bin/env python

import piglow
from time import sleep

piglow.auto_update = True
BRIGHT_MAX = 20
bright = BRIGHT_MAX

for count in range(4):
    for x in reversed(range(6)):
        arr = [x, x + 6, x + 12]
        piglow.set(arr, bright)
        sleep(0.1)
    
    bright = 0 if bright == BRIGHT_MAX else BRIGHT_MAX
