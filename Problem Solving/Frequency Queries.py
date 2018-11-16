def freqQuery(queries):

    ans = []
    arr = Counter()
    cnt = Counter()

    for q in queries:
        if q[0] == 1:
            cnt[arr[q[1]]] -= 1
            arr[q[1]] += 1
            cnt[arr[q[1]]] += 1
        elif q[0]==2:
            if arr[q[1]] > 0:
                cnt[arr[q[1]]] -= 1
                arr[q[1]] -= 1
                cnt[arr[q[1]]] += 1
        else:
            ans.append(int(cnt[q[1]]>0))

    return ans
