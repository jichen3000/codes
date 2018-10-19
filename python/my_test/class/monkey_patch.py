class System:
    def mm(self):
        return "mm"
    def nn(self):
        return "nn"


# cannot use this way, no nn function
# class System:
#     def mm(self):
#         return "mm1"
def mm(self):
    return "mm1"
System.mm = mm

if __name__ == '__main__':
    from minitest import *

    with test(System):
        system = System()
        system.mm().must_equal("mm1")
        system.nn().must_equal("nn")
