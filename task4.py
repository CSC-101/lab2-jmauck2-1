from typing import Optional

def checked_access(L:list[int], idx:int) -> Optional[int]:
    test = idx >= 0 and idx < len(L)        #first: False, second: True
    if test:                                #This test prevents an error where the code is indexing a value outside of the string.
        return L[idx]
    else:
        return None

first = checked_access([1, 0, 1], 9)        #first = none
print("first: ", first)
second = checked_access([1, 0, 1], 2)       #second = 1
print("second: ", second)

def length_sum(L:list[str]) -> int:
    if len(L) > 2:
        result = len(L[0]) + len(L[1]) + len(L[2])  #This call is evaluated for "first" only. The length of the strings in position 0, 1, & 2 of the argument are being added.
    elif len(L) > 1:
        result = len(L[0]) + len(L[1])              #This call is evaluated for "third" only. The length of the strings in position 0 & 1 of the argument are being added.
    elif len(L) > 0:
        result = len(L[0])                          #This call is evaluated for "second" only. This value is the length of the string in position 0 pf the argument is being returned.
    else:
        result = 0
    return result

first = length_sum(["this", "is", "the", "first", "call"])
second = length_sum(["second call"])
third = length_sum(["another", "call"])
print(first, second, third)

def surprising(L:list[str], other:str) -> list[str]:
    L.append(other.upper())
    return L

words = ["this", "is", "confusing", "code."]
first = surprising(words, "Avoid")
second = surprising(words, "such.")
print(words, first, second)

#The value of words is ['this', 'is', 'confusing', 'code.', 'AVOID', 'SUCH.']
#The value of first and second are the same as "words" at this point.
#The variables "first" and "second" are not new lists, instead they are new names for the original list "words." Because lists are mutable the changes from "surprising" apply to all variables.
