import cql

def print_and_execute(cursor, cql_str):
    print("cql: %s"%cql_str)
    result=cursor.execute(query)
    print("result: %s"%result)
    if cursor.rowcount > 0:
        print("rowcount: %d"%cursor.rowcount)
        for row in cursor:
            print row

    return result

def patch_method(target, method):
    import types
    setattr(target, method.func_name, types.MethodType(method,target))


host, port = "199.167.199.151", 9160
keyspace = "mykeyspace"

con = cql.connect(host, port, cql_version='3.0.0')
print con

cursor = con.cursor()

patch_method(cursor, print_and_execute)

query="use %s;"%keyspace
cursor.print_and_execute(query)

query="select * from users;"
cursor.print_and_execute(query)
# print cursor.rowcount

cursor.close()
con.close()

print 'ok'