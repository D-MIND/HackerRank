def arrayManipulation(n, queries):
    vals = [0] * (n+1)
    count = temp = 0
    for a,b,c in queries:
        vals[a-1] += c
        vals[b] -= c
    for val in vals:
        count += val
        if count > temp:
            temp = count
    return temp
