def maxMin(k, arr):
    arr = sorted(arr)
    return min([(y - x) for x,y in zip(arr[0:], arr[k-1:])])
