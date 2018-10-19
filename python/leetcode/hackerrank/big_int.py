class BigInt(object):
    def __init__(self, number, base=10):
        self.base = base
        if type(number) == list:
            self.data_arr = number
        else:
            self.data_arr = []
            index = 0
            cur_base = base
            left_number = number
            while index < 100 and left_number > 0:
                left_number, cur_value = divmod(left_number, base)
                self.data_arr.append(cur_value)
                index += 1

    def __repr__(self):
        return "{}({}, base={})".format(self.__class__.__name__,
                self.data_arr, self.base)

    def multiple_single(self, the_n):
        if the_n >= self.base:
            raise Exception("Cannot handle the number({}) > {}".format(
                    the_n, self.base))
        carry = 0
        # import ipdb; ipdb.set_trace()
        for i in xrange(len(self.data_arr)):
            carry, new_value = divmod(self.data_arr[i] * the_n + carry, self.base) 
            self.data_arr[i] = new_value
        if carry > 0:
            self.data_arr.append(carry)

        return self

    # def 

    # def multiple(self, other):
    #     if other.base != self.base:
    #         raise Exception("only support same base! {} != {}".format(
    #                 other.base, self.base))

    #     cur_base = self.base
    #     origin_data_arr = self.data_arr[:]
    #     for value in other.data_arr:
    #         self.multiple_single(value)



    def number(self):
        the_number = 0
        cur_base = 1
        for value in self.data_arr:
            the_number += value * cur_base
            cur_base *= self.base
        return  the_number

    @staticmethod
    def factial(n):
        base = 2**32
        if n > base:
            raise Exception("not support!")
        big_int = BigInt(1, base)
        for i in range(n):
            big_int.multiple_single(i+1)
        return big_int


if __name__ == '__main__':
    from minitest import *

    with test(BigInt):
        a = BigInt(132)
        a.data_arr.must_equal([2, 3, 1])
        a.number().must_equal(132)
        # a.multiple_single(10).number().p()
        a.multiple_single(9).number().must_equal(1188)

        b = BigInt.factial(25)
        b.data_arr.p()
        b.number().must_equal(15511210043330985984000000)




