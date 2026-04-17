def smallest(n:float, m:float):
    if n < m:
        return n        #none
    else:
        return m
first = smallest(3,2)       #first = 2
second = smallest(2,2)      #second = 2, this is not reasonable because n and m are equal
print()

def function2(a:int, b:int, c:int) -> int:
    if a > b and a > c:
        return a - b    #When a is the largest input value.
    elif b > c:
        return b + c    #When b is greater than or equal to c and a is less than or equal to b or c
    else:
        return 2 * c    #When a is less than b or c and c is greater than or equal to b.

answer1 = function2(3, 2, 1)    #1
answer2 = function2(2, 3, 1)    #4
answer3 = function2(2, 1, 3)    #6
print(answer1)
print(answer2)
print(answer3)