import re

TYPE_INI = "ini"
TYPE_XML = "xml"

def replace_all_with_type(items):
    return [replace_one_file_with_type(item['file_path'],
                                        item['fun_type'],
                                        item['source_key'],
                                        item['replace_value'],
                                        item.get('suffix_write_file_path',""))
        for item in items]

# just two type: ini, xml
def replace_one_file_with_type(file_path, fun_type, source_key, replace_value, suffix_write_file_path=""):
    return replace_one_file_with_re(file_path,
        globals()['__generate_re_pattern_4'+fun_type](source_key),
        globals()['__generate_replace_str_4'+fun_type](replace_value),
        suffix_write_file_path)

def replace_one_file_with_re(file_path, re_pattern, replace_str, suffix_write_file_path=""):
    lines = __read_lines(file_path)
    lines = [re.sub(re_pattern, replace_str, line) for line in lines]
    return __write_lines(file_path+suffix_write_file_path, lines)

def to_raw_string(str):
    return str.replace('\\', '\\\\\\\\')

# source_key="LogFilePath"
# return value="(\<LogFilePath.*\>).+(\<\/LogFilePath\>)"
def __generate_re_pattern_4xml(source_key):
    return "(\<"+source_key+".*\>).+(\<\/"+source_key+"\>)"
            
# replace_value="/usr/colin/"
# return value=r"\1/usr/colin/\2"
def __generate_replace_str_4xml(replace_value):
    return r"\1"+to_raw_string(replace_value)+r"\2"

# source_key="DownloadFileDestination"
# return value="(\s*DownloadFileDestination\s*=\s*).+"
def __generate_re_pattern_4ini(source_key):
    return "(\s*"+source_key+"\s*=\s*).+"
            
# replace_value='"/usr/colin/"'
# return value=r'\1"/usr/ini/"'
def __generate_replace_str_4ini(replace_value):
    return r"\1"+to_raw_string(replace_value)

def __add_newline_if_need(lines):
    return [ line+'\n' if not line.endswith('\n') else line for line in lines]

def __write_lines(file_path, lines):
    new_lines = __add_newline_if_need(lines)
    with open(file_path, 'w') as f:
        f.writelines(new_lines)
    return True

def __read_lines(file_path):
    with open(file_path, 'r') as f:
        return f.readlines()



def test():
    lines = ['111','222']
    print "lines:", __add_newline_if_need(lines)
    lines = ['111\n','222\n']
    print "lines:", __add_newline_if_need(lines)
    re_pattern = "(\<LogFilePath.*\>).+(\<\/LogFilePath\>)"
    replace_str = r"\1"+to_raw_string("c:\\")+r"\2"
    file_path = "a.xml"
    replace_one_file_with_re(file_path, __generate_re_pattern_4xml("LogFilePath"),
        replace_str,'.bak')
    replace_one_file_with_type(file_path, TYPE_XML, "LogFilePath",
        "/usr/colin/",'.bak1')


    re_pattern = "(\s*DownloadFileDestination\s*=\s*).+"
    replace_str = r'\1"/usr/ini/"'
    file_path = "a.ini"
    replace_one_file_with_re(file_path, __generate_re_pattern_4ini("DownloadFileDestination"), 
        __generate_replace_str_4ini('"/usr/ini/"'),".bak")
    replace_one_file_with_type(file_path, TYPE_INI, "DownloadFileDestination",
        '"/usr/ini/"','.bak1')


    print __generate_re_pattern_4xml("LogFilePath")
    print __generate_replace_str_4xml("/usr/colin/")

    needed_replace_files = [{'file_path':"a.xml",
                        'fun_type':TYPE_XML,
                        'source_key':"LogFilePath",
                        'replace_value':"c:\\",
                        'suffix_write_file_path':'.all'},
                    {'file_path':"a.ini",
                        'fun_type':TYPE_INI,
                        'source_key':"DownloadFileDestination",
                        'replace_value':'"/usr/ini/"',
                        'suffix_write_file_path':'.all'}]

    replace_all_with_type(needed_replace_files)


if __name__ == '__main__':
    test()