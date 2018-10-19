# http://stackoverflow.com/questions/3372444/profile-memory-allocation-in-python-with-support-for-numpy-arrays

import numpy
# @profile
# def my_func():
#     a = [1] * (10 ** 6)
#     b = [2] * (2 * 10 ** 7)
#     del b
#     return a

# @profile
# def for_numpy():
#     numpy.random.seed(2)
#     a = numpy.random.rand(1e7)
#     b = [numpy.partition(a, 10000) for i in range(100)]

# @profile
# def for_numpy():
#     numpy.random.seed(2)
#     a = numpy.random.rand(1e7)
#     for i in range(100):
#         b = numpy.partition(a, numpy.random.randint(1e6))
#         b[0] = 1.1

@profile
def for_numpy():
    numpy.random.seed(2)
    a = numpy.random.rand(1e7)
    for i in range(100):
        a.partition(numpy.random.randint(1e6))


if __name__ == '__main__':
    for_numpy()
    # python -m memory_profiler profiler_test.py


# Filename: profiler_test.py
#
# Line #    Mem usage    Increment   Line Contents
# ================================================
#     11   23.543 MiB    0.000 MiB   @profile
#     12                             def for_numpy():
#     13   23.543 MiB    0.000 MiB       numpy.random.seed(2)
#     14   99.859 MiB   76.316 MiB       a = numpy.random.rand(1e7)
#     15 2532.914 MiB 2433.055 MiB       b = [numpy.partition(a, 10000) for i in range(100)]
#
# Line #    Mem usage    Increment   Line Contents
# ================================================
#     18   23.551 MiB    0.000 MiB   @profile
#     19                             def for_numpy():
#     20   23.551 MiB    0.000 MiB       numpy.random.seed(2)
#     21   99.867 MiB   76.316 MiB       a = numpy.random.rand(1e7)
#     22  252.551 MiB  152.684 MiB       for i in range(100):
#     23  252.551 MiB    0.000 MiB           b = numpy.partition(a, numpy.random.randint(1e6))
#     24  252.551 MiB    0.000 MiB           b[0] = 1.1

    # Line #    Mem usage    Increment   Line Contents
    # ================================================
    #     25   23.613 MiB    0.000 MiB   @profile
    #     26                             def for_numpy():
    #     27   23.613 MiB    0.000 MiB       numpy.random.seed(2)
    #     28   99.934 MiB   76.320 MiB       a = numpy.random.rand(1e7)
    #     29  100.004 MiB    0.070 MiB       for i in range(100):
    #     30  100.004 MiB    0.000 MiB           a.partition(numpy.random.randint(1e6))
