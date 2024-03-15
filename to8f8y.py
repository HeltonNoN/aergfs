def f(arr):
    if len(arr)<=1:
        return arr
    else:
        bzn=arr[0]
        left=[x for x in arr[1:] if x<bzn]
        right=[x for x in arr[1:] if x>=bzn]
        return f(left)+[bzn]+f(right)
arr=[3,1,4,2,4]
print(f(arr))

import random
random.choise(string)
