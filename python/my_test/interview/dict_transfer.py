def transfer(input):
    result = {}
    for item in input:
        if item.get('age', 40) >= 10 and item.get('age', 40) <40:
            if result.get('adults') == None:
                result['adults'] = []
            result['adults'].append(item['name'])
        elif item.get('age', 40) < 10:
            if result.get('kids') == None:
                result['kids'] = []
            result['kids'].append(item['name'])
        else:
            if result.get('old') == None:
                result['old'] = []
            result['old'].append(item['name'])
    return result

if __name__ == '__main__':
    from minitest import *
    with test(transfer):
        transfer([
            {"name":"abc","age":5},
            {"name":"xyz","age":20},
            {"name":"pqr","age":60}, 
            {"name":"efg"}]).must_equal(
            {'kids': ['abc'], 'old': ['pqr', 'efg'], 'adults': ['xyz']})