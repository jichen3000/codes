def flatten1(lst):
    return [item for sublist in lst for item in sublist]

def flatten(lst):
    result = []
    for sublist in lst:
        if isinstance(sublist, list):
            for item in sublist:
                result.append(item)
        else:
            result.append(sublist)
    return result


print flatten([[12,34],5,6])