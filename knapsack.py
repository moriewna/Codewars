# Knapsack problem. Solution 1 - greedy algorithm (value/size)

def knapsack(capacity, items):
    items_copy = sorted(items, key=lambda tup: tup[1]/float(tup[0]), reverse=True)
    totcap = 0
    res = [0 for a in range(len(items_copy))]
    while totcap <= capacity and len(items_copy) > 0:
        c = capacity - totcap
        nr = int(c/items_copy[0][0])
        if nr == 0 : items_copy.pop(0)
        else :
            res[items.index(items_copy[0])] += 1*nr
            totcap += (nr*items_copy[0][0])
    return res

# print knapsack(100, ((11.2,  7.4),
                                  (25.6, 17.8),
                                  (51.0, 41.2),
                                  (23.9, 15.6),
                                  (27.8, 19.0)))
