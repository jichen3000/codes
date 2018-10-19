import redis
import datetime
from json import dumps, loads

# def json_serial(obj):
#     """JSON serializer for objects not serializable by default json code"""

#     if isinstance(obj, (datetime.datetime, datetime.date)):
#         return obj.isoformat()
#     raise TypeError ("Type %s not serializable" % type(obj))

# def json_dumps_ext(obj):
#     return json.dumps(obj, default=json_serial)
# # connection pool
# # pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
# # r = redis.StrictRedis(connection_pool=pool)

def get_dict(id):
    now = get_now()
    return {
        "id":id,
        "some" : {"1":1, "2":2},
        "date" : now,
        "is_true" : True,
        "list" : [{"1":1, "2":2},{"1":now, "2":False}],
        "none" : None
    }
def get_now():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")    

class TestObject:
    def __init__(self, r, id_name = "id"):
        self.id_list_name = self.__class__.__name__.lower() + "_id_list"
        self.hash_name = self.__class__.__name__.lower() + "_hash"
        self.id_name = id_name
        self.r = r

    def add_or_update(self, obj):
        old_obj = self.get(obj[self.id_name])
        if old_obj == None:
            self.r.lpush(self.id_list_name, obj[self.id_name])
        self.r.hset(self.hash_name, obj[self.id_name], dumps(obj))
        return obj

    def get(self, obj_id):
        obj_str = self.r.hget(self.hash_name, obj_id)
        if obj_str:
            return loads(obj_str)

    def get_list(self, start=0, end=-1):
        id_list = self.r.lrange(self.id_list_name, start, end)
        return [self.get(obj_id) for obj_id in id_list]

    def delete(self, obj_id):
        old_obj = self.get(obj_id)
        if old_obj:
            for index, obj in enumerate(self.get_list()):
                # obj.pp()
                if obj[self.id_name] == obj_id:
                    r.hdel(self.hash_name, obj_id)
                    r.lset(self.id_list_name, index, "DELETED")
                    r.lrem(self.id_list_name, 1, "DELETED")
                    return old_obj


        

if __name__ == '__main__':
    from minitest import *

    # decode_responses, string not b'' any more
    # When set to True the client will decode the responses using the encoding option. By default encoding = utf-8.
    r = redis.StrictRedis(host='redis-test', port=6379, db=0, decode_responses=True)
    # with test("linked list"):
    #     r.delete("dict_list")
    #     the_list = list(map(json_dumps_ext, map(get_dict, range(3))))
    #     r.lpush("dict_list", *the_list)
    #     aa = r.lrange("dict_list", 0, 20)
    #     aa.pp()
    #     json.loads(aa[0])["id"].p()
    with test(TestObject):
        to = TestObject(r)
        r.delete(to.id_list_name)
        r.delete(to.hash_name)
        to.get("1").must_equal(None)
        obj1 = get_dict("1")
        to.add_or_update(obj1)
        to.get("1").must_equal(obj1)
        obj1["is_true"] = False
        to.add_or_update(obj1)
        to.get("1").must_equal(obj1)
        obj2 = get_dict("2")
        to.add_or_update(obj2)
        to.get("2").must_equal(obj2)
        obj_3_9 = [to.add_or_update(get_dict(str(i))) for i in range(3,10)]
        all_objs = [obj1, obj2] + obj_3_9
        all_objs = all_objs[::-1]
        to.get_list().must_equal(all_objs)
        to.get_list(4, 6).must_equal(all_objs[4:7])

        to.delete("100").must_equal(None)
        del_obj = all_objs.pop(3)
        to.delete(del_obj["id"]).must_equal(del_obj)
        to.get_list().must_equal(all_objs)

