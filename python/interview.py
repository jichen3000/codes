
def duplicate(str1):
    return ''.join ([ c for c in str1])
    # result = [if c not in result for c in str1]


def remove_duplicates(str1):
    result = []
    for c in str1:
        if c not in result:
            result.append(c)

    return ''.join(result)

str1 = 'fortinet'
str2 = duplicate(str1)
print str2
