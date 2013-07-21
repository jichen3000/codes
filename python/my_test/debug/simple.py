# -*- coding: utf-8 -*-
# http://docs.python.org/2/library/pdb.html
# break 或 b   设置断点
# continue    或 c 继续执行程序
# list 或 l    查看当前行的代码段
# step 或 s    进入函数
# return 或 r  执行代码直到从当前函数返回
# exit 或 q    中止并退出
# next 或 n    执行下一行
# pp  打印变量的值
# help    帮助

# break d.py:6
# break d.py:6, sum > 50
# break d.main

def main():
        i, sum = 1, 0
        for i in xrange(100):
            print "now sum is %d" % sum
            sum = sum + i
        print sum

if __name__ == '__main__':
        main()
