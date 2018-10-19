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

e = EasyDict(foo=3)
print(e.foo)