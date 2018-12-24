def getMinimumCost(k, c):
    return sum([cost * ((i // k) + 1) for i, cost in enumerate(sorted(c, reverse=True))])
