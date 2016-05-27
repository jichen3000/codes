import pdb

def main():
        i, sum = 1, 0
        pdb.set_trace()
        # import ipdb; ipdb.set_trace()
        for i in xrange(100):
                sum = sum + i
        print sum

if __name__ == '__main__':
        main()
