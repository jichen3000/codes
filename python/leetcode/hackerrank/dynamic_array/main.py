n,m = map(int, raw_input().strip().split(" "))
s_list = [[] for i in xrange(n)]
last_answer = 0
for i in xrange(m):
    query_type, x, y = map(int, raw_input().strip().split(" "))
    if query_type == 1:
        s_index = (x+last_answer) % n
        s_list[s_index].append(y)
    elif query_type == 2:
        print(query_type, x, y)
        s_index = (x+last_answer) % n
        print(s_index)
        for index, ss in enumerate(s_list):
            if len(ss)>0: print(index, ss)
        inner_index = y % len(s_list[s_index])
        last_answer = s_list[s_index][inner_index]
        print last_answer