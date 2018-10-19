import importlib
class Device:
    def __init__(self, package_name):
        self.package_name = package_name
        self.dynamic_import()

    def dynamic_import(self):
        common_module = importlib.import_module('device_common')
        name_module_map = {name:common_module for name in common_module.__all__}
        if self.package_name != "device_common":
            special_module = importlib.import_module(self.package_name)
            name_module_map.update({name:special_module for name in special_module.__all__}) 
        for attr_name, module in name_module_map.items():
            class_module = importlib.import_module(name_module_map[attr_name].__name__+"."+attr_name)
            camel = "".join(map(str.capitalize, attr_name.split("_")))
            the_obj = getattr(class_module,camel)()
            setattr(self, attr_name, the_obj)

if __name__ == '__main__':
    from minitest import *

    with test(Device):
        d6000 = Device("device_6000") 
        d6000.firewall.some().must_equal("device_common.firewall.Firewall")
        d6000.system.some().must_equal("device_6000.system.System")

        d7000 = Device("device_7000") 
        d7000.firewall.some().must_equal("device_7000.firewall.Firewall")
        d7000.load_balance.some().must_equal("device_7000.load_balance.LoadBalance")
        d7000.system.some().must_equal("device_7000.system.System")
        d7000.system.common().must_equal("common")
        d7000.system.special().must_equal("special")
