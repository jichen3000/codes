import traceback
class SomeObject():
    def __init__(self, def_name=None):
        if def_name == None:
            (filename,line_number,function_name,text) = \
                traceback.extract_stack()[-2]
            print traceback.extract_stack()
            def_name = text[:text.find('=')].strip()
        self.instance_name = def_name

this = SomeObject()
print this.instance_name