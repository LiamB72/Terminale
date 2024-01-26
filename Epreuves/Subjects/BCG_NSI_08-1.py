def max_dico(d: dict):
    maxLike = 0
    maxName = ""
    for name in d:
        if d[name] > maxLike:
            maxLike, maxName = d[name], name

    print((maxName, maxLike))
    return maxName, maxLike


max_dico({'Bob': 102, 'Ada': 201, 'Alice': 103, 'Tim': 50})
max_dico({'Alan': 222, 'Ada': 201, 'Eve': 220, 'Tim': 50})
