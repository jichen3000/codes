import redis

# connection pool
# pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
# r = redis.StrictRedis(connection_pool=pool)

if __name__ == '__main__':
    from minitest import *

    # decode_responses, string not b'' any more
    # When set to True the client will decode the responses using the encoding option. By default encoding = utf-8.
    r = redis.StrictRedis(host='redis-test', port=6379, db=0, decode_responses=True)
    with test("string"):
        r.set("test", 123)
        r.get("test").must_equal("123")

    with test("linked list"):
        r.delete("mylist")
        r.lpush("mylist", 1, 2, 3)
        aa = r.lrange("mylist", 0, -1)
        aa.must_equal(['3', '2', '1'])

    with test("set"):
        r.sadd("myset", 1, 2, 3)
        r.smembers("myset").must_equal({'3', '2', '1'})

    with test("sorted set"):
        r.zadd("hackers", 1940, "Alan Kay")
        r.zadd("hackers", 1957, "Sophie Wilson")
        r.zadd("hackers", 1953, "Richard Stallman")
        r.zadd("hackers", 1949, "Anita Borg")
        r.zadd("hackers", 1965, "Yukihiro Matsumoto")
        r.zadd("hackers", 1914, "Hedy Lamarr")
        r.zadd("hackers", 1916, "Claude Shannon")
        r.zadd("hackers", 1969, "Linus Torvalds")
        r.zadd("hackers", 1912, "Alan Turing")
        r.zrange("hackers",0,-1).must_equal([
                'Alan Turing',
                'Hedy Lamarr',
                'Claude Shannon',
                'Alan Kay',
                'Anita Borg',
                'Richard Stallman',
                'Sophie Wilson',
                'Yukihiro Matsumoto',
                'Linus Torvalds'])

    with test("hash"):
        id = "user:1000"
        r.delete(id)
        user = {"Name":"Pradeep", "Company":"SCTL", "Address":"Mumbai"}
        # r.hmset("user:1000", user)
        r.hset(id, "Name", "Pradeep")
        r.hset(id, "Company", "SCTL")
        r.hset(id, "Address", "Mumbai")
        r.hget("user:1000", "Name").must_equal("Pradeep")
        r.hgetall("user:1000").must_equal(user)

