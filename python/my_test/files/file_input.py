import fileinput

print("please input the string which you want to decode:")
for line in fileinput.input():
    break

print(line)
print("ok")


def main():
    n_list = None
    n_max = 0
    for line in fileinput.input(files="test.txt"):
        if fileinput.lineno() == 1:
            n, m = map(int, line.split(" "))
            n_list = [0 for i in range(n)]
        else:
            start_index, end_index, value =  map(int,line.split(" "))
            for i in range(start_index-1, end_index):
                n_list[i] += value
                if n_list[i] > n_max: n_max = n_list[i]
    print(n_max)

main()
