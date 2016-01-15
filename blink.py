#!/usr/bin/env python

import piglow
import sys
from time import sleep

piglow.auto_update = True

argv = sys.argv
color = 'all'

if len(argv) > 1:
    color = argv[1]

method = getattr(piglow, color)

# shine once
for x in range(180):
    method(x)
    piglow.show()
for x in reversed(range(180)):
    method(x)
    piglow.show()
