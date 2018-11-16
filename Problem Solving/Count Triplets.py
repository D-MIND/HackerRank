def countTriplets(arr, r):
    count = 0
    dr = defaultdict(int)
    drr = defaultdict(int)

    for elem in arr:
        count += drr[elem]
        drr[elem*r] += dr[elem]
        dr[elem*r] += 1

    return count
