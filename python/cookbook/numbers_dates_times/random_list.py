import random
import time
from minitest import *

values = range(6)
# if I don't sleep a while, sometimes I will get same value.
random.choice(values).p()
time.sleep(0.1)
random.choice(values).p()
time.sleep(0.1)
random.choice(values).p()
time.sleep(0.1)
random.choice(values).p()
time.sleep(0.1)
random.choice(values).p()
time.sleep(0.1)

random.sample(values,2).p()

random.shuffle(values)
values.p()

random.randint(0,10).p()

random.random().p()

random.getrandbits(20).p()