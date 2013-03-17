def gen_99():
	return [(i,j) for i in range(9) for j in range(9)]

b = ((i,j,k) for i in range(2) for j in range(3) for k in range(4))
print b
print [(i,j,k) for i,j,k in b]
if __name__ == '__main__':
	print gen_99()