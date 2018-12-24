def whatFlavors(cost, money):
    map = {}
    for idx, price in enumerate(cost):
        if price in map:
            print(*[map[price], idx + 1], sep = " ")
        else:
            map[money-price] = idx + 1
