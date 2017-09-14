'''
Created on Sep 7, 2017

@author: jlearx
'''

import random

if __name__ == '__main__':
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    c = []
    
    # One line solution
    [c.append(e) for e in a+b if ((e in a) and (e in b) and (c.count(e) == 0))]
    print(c)
    
    # Randomly generate Lists
    print("Randomly generating lists...")
    a.clear()
    b.clear()
    c.clear()
    seed = random.seed()
    
    # Populate A
    count = random.randint(1,100)
    [a.append(random.randint(1,100)) for i in range(1, count + 1)]
    print("List a = ", end="")
    print(a)
    
    # Populate B
    count = random.randint(1,100)
    [b.append(random.randint(1,100)) for i in range(1, count + 1)]
    print("List b = ", end="")    
    print(b)
    
    # Determine Overlapped
    # One line solution
    [c.append(e) for e in a+b if ((e in a) and (e in b) and (c.count(e) == 0))]
    print("Overlap:")
    print(c)
        