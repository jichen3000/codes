class RemoveList(object):
    def __init__(self, init_list=None):
        self.pos_dict = {}
        self.l = []
        if init_list:
            for i in init_list:
                self.append(i)
            

    def append(self, item):
        self.pos_dict[item] = len(self.l)
        self.l.append(item)

    def remove(self, item):
        last = self.l[-1]
        last_i = self.pos_dict[last]
        cur_i = self.pos_dict[item]
        self.pos_dict[last] = cur_i
        self.l[cur_i], self.l[last_i] = self.l[last_i], self.l[cur_i]
        del self.pos_dict[item]
        self.l.pop()

    def move_to_last(self, item):
        last = self.l[-1]
        last_i = self.pos_dict[last]
        cur_i = self.pos_dict[item]
        self.pos_dict[last], self.pos_dict[item] = cur_i, last_i
        self.l[cur_i], self.l[last_i] = self.l[last_i], self.l[cur_i]

    def __len__(self):
        return len(self.l)

if __name__ == '__main__':
    from minitest import *

    with test(RemoveList):
        rl = RemoveList()
        rl.append(5)
        rl.append(6)
        rl.append(7)
        rl.remove(6)
        rl.l.must_equal([5,7])

        rl = RemoveList([5,6,7])
        rl.remove(6)
        rl.l.must_equal([5,7])

        rl.move_to_last(5)
        rl.l.must_equal([7,5])
