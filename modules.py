import sys
#print(sys.path)

import re

text = "mi numero es 1234"

result = re.findall("[0-9]+", text)

print(result)

import time

timestamp = time.time()
print(timestamp)

local = time.localtime()
print(local)

formatted = time.asctime(local)
print(formatted)


import collections

numbers = [1, 1,2,3,1,2,45,8,965,3,32,1]
counter = collections.Counter(numbers)
print(counter)