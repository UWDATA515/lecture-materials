def hist(dictionary):
    result = {}
    for v in dictionary.values():
        if v in result:
            result[v] += 1
        else:
            result[v] = 1
    return result
