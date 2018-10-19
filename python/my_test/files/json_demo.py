from easydict import EasyDict
import simplejson
j = """{
"Buffer": 12,
"List1": [
    {"type" : "point", "coordinates" : [100.1,54.9] },
    {"type" : "point", "coordinates" : [109.4,65.1] },
    {"type" : "point", "coordinates" : [115.2,80.2] },
    {"type" : "point", "coordinates" : [150.9,97.8] }
]
}"""

d = EasyDict(simplejson.loads(j))
print(d)
print(d.Buffer)

import json

def dump(content, filepath):
    json.dump(content, open(filepath,'w'), indent = 4)
    return content

def load(filepath):
    # the_file = open(filepath)
    # import ipdb; ipdb.set_trace()
    return json.load(open(filepath))

def append_dump(content, filepath):
    with open(filepath,'a') as the_file:
        json.dump(content, the_file, indent = 4)
    return content



if __name__ == '__main__':
        from minitest import *
    
        # with test(append_dump):
        #     filepath = "test.json"
        #     for i in range(3):
        #         content = {"index":i,"some":"m"*i}
        #         append_dump(content, filepath)    