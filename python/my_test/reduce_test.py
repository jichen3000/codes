def append_one(result,cur):
	print result,cur
	result.append(cur)
	return result

a = [1,2,3]
print reduce(append_one,a,[])