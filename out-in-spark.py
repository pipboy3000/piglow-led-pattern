#!/usr/bin/env python

import piglow
from time import sleep

piglow.auto_update = True

for count in range(4):
    for x in range(6):
        list = [x, x + 6, x + 12]
        piglow.set(list, 20)
        sleep(0.05)
        piglow.set(list, 0)
        sleep(0.03)
