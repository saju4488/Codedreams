

import random

from more_itertools import tail
from regex import P



head = """
     _.-._
   .' | | `.
  /   | |   \
 |    | |    |
 |____|_|____|
 |____(_)____|
 /|(o)| |(o)|\
/ |   | |   | \
\ |  (|_|)  | /
 | \/     \/ |
 / /  ___  \ \  앞
(             )
 \           /
 `._______.'
"""

fail = """
     _.-._
   .' | | `.
  /   | |   \
 |    | |    |
 |____|_|____|
 |____(_)____|
 /|(o)| |(o)|\
//|   | |   |\\
'/|  (|_|)  |\`
 //.///|\\\.\\
 /////---\\\\\  뒤
 ////|||||\\\\
 '//|||||||\\`
   '|||||||`
"""

print("게임에 오신것을 환영합니다.")

computer = random.randint(0,1)
choice = int(input("앞면일까요? 뒷면일까요? 0:앞면, 1:뒷면 \n"))

print("동전결과:")
if computer == 0:
    print(head)
else:
    print(tail) 

print("나의선택:")       
if choice == 0:
    print(head)
else:
    print(tail)    

print("게임결과:")
if computer == choice:
    print("적중!!")
else:
    print("아쉽네요. 틀렸습니다.")    
