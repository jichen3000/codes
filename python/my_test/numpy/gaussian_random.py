import numpy

if __name__ == '__main__':
    from minitest import *

    with test("show gaussian random"):
        count = 1000
        numpy.random.seed(2)
        all_nums = [numpy.random.normal() for i in range(1000)]
        sum_v = numpy.sum(all_nums)
        mean_v = sum_v / count
        min_v = min(all_nums)
        max_v = max(all_nums)
        mean_v.p()
        min_v.p()
        max_v.p()
        pass
# ('mean_v :', 0.045099590046984772)
# ('min_v :', -3.4999002466579747)
# ('max_v :', 3.221271861831951)
