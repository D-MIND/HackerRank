def isValid(s):
    counter = {}

    for word in s:
        try:
            counter[word] += 1
        except KeyError:
            counter[word] = 1

    values = list(counter.values())
    mymax = max(values)
    mymin = min(values)
    if mymax == mymin or (mymax - mymin == 1 and values.count(mymax) == 1) or (mymin == 1 and values.count(mymin) == 1 and len(set(values)) == 2):
        return "YES"
    else:
        return "NO"
