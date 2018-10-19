import device_common.system
class System(device_common.system.System):
    def some(self):
        return self.__class__.__module__+"."+self.__class__.__name__
    def special(self):
        return "special"
