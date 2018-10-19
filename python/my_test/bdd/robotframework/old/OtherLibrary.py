from robot.libraries.BuiltIn import BuiltIn

class OtherLibrary:
    def __init__(self):
        pass

    def print_variables(self):
        print "*WARN* all variables." + str(BuiltIn().get_variables())
