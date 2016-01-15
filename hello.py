#!/usr/bin/env python

import piglow
from time import sleep

piglow.auto_update = True

# blink 3 times
BRIGHT_MAX = 20
bright = BRIGHT_MAX

for count in range(4):
    for x in range(6):
        list = [x, x + 6, x + 12]
        piglow.set(list, bright)
        sleep(0.1)
    
    bright = 0 if bright == BRIGHT_MAX else BRIGHT_MAX

# shine once
for x in range(130):
    piglow.all(x)
    piglow.show()
for x in reversed(range(130)):
    piglow.all(x)
    piglow.show()
