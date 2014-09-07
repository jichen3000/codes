class Modle(object):
    def __init__(self):
        self.on_changes = []
    def set_on_change(self,func):
        self.on_changes.append(func)
    def changed(self):
        for cur_func in self.on_changes:
            cur_func(self)

class Staff(Modle):
    pass


if __name__ == '__main__':
    def print1(staff):
        print("11")
    def print2(staff):
        print("22")
    class StaffControler(object):
        def on_staff_change(self, staff):
            print(staff)
    def main():
        staff = Staff()
        staff.set_on_change(print1)
        staff.set_on_change(print2)
        staff_controler = StaffControler()
        staff.set_on_change(staff_controler.on_staff_change)
        staff.changed()
    main()
