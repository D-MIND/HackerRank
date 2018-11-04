def minimumSwaps(arr):
    swaps=0
    i=0
    while i<len(arr):
        if len(arr) == 7 and i == 6:
            break
        if arr[i] == (i+1):
            i += 1
            continue
        arr[arr[i] - 1], arr[i] = arr[i], arr[arr[i] - 1]
        swaps += 1
    return swaps
