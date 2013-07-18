import inspect
from pprint import pprint as pp

def hello():
    pp(inspect.getouterframes(
        inspect.currentframe()))
    frame,filename,line_number,function_name,lines,index=\
        inspect.getouterframes(inspect.currentframe())[1]
    print(frame,filename,line_number,function_name,lines,index)

    file_info = inspect.getouterframes(inspect.currentframe())[1]
    print(file_info[1]+":"+str(file_info[2]))


hello()
