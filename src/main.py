'''
Created on Sep 7, 2017

@author: jlearx
'''

if __name__ == '__main__':
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    c = []
    
    # One line solution
    
    [c.append(e) for e in a+b if ((e in a) and (e in b) and (c.count(e) == 0))]

    print(c)
    
    