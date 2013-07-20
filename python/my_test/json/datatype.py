import json

print json.dumps({'4': 5, '6': 7}, sort_keys=True,
                 indent=4, separators=(',', ': '))

filename = 'datatype.json'
tree =  \
            {'no surfacing': 
                {0: 'no', 
                 1: {'flippers': 
                        {0: 'no', 
                         1: 'yes'}}}}

with open(filename,'w') as output:
    # output.write(json.dumps({'4': 5, '6': 7}, sort_keys=True,
    #              indent=4, separators=(',', ': ')))
    output.write(json.dumps(tree, sort_keys=True,
                 indent=4, separators=(',', ': ')))

with open(filename, 'r') as output:
    print json.loads(output.read())