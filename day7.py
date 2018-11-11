# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message,
# count the number of ways it can be decoded.
#
# For example, the message '111' would give 3, since it could be decoded as 'aaa, 'ka', and 'ak'.

import numpy as np
from math import factorial

message = '1111'

# every 2 #'s <=26 can be decoded as a letter or 2 letters - 2 interpretations per,

sings = 1 #case where all digits are letters (ignoring 0's for now)
dbls = 0

for i, digit in enumerate(message):
    if i+1 < len(message) and int(message[i+1]) <= 6 and int(digit) <= 2 and int(digit) != 0:
        dbls += 1
ans = sings + factorial(dbls) #permute and add base case
print(ans)

