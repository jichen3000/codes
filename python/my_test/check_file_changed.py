import sys
import os
import hashlib
import json

result_file_path = os.path.join(os.path.dirname(
    os.path.realpath(__file__)), 'files.dat')
backup_result_file_path = os.path.join(os.path.dirname(
    os.path.realpath(__file__)), 'files.dat.bak')


def get_all_file_paths(file_path):
    return [os.path.join(dirpath,filename) 
        for (dirpath, dirnames, filenames) in os.walk(file_path) 
        for filename in filenames]

def gen_file_md5(file_path, block_size=1048576):
    md5 = hashlib.md5()
    with open(file_path, 'rb') as file:
        while True:
            data = file.read(block_size)
            if not data:
                break
            md5.update(data)
    return md5.hexdigest()

def write_to_json(file_path, obj):
    with open(file_path, 'w') as file:
        file.write(json.dumps(obj, 
            sort_keys=True, indent=4, separators=(',', ': ')))

def read_from_json(file_path):
    result = None
    with open(file_path, 'r') as file:
        result = json.loads("".join(file.readlines()),object_hook=_decode_dict)
    return result

def _decode_list(data):
    rv = []
    for item in data:
        if isinstance(item, unicode):
            item = item.encode('utf-8')
        elif isinstance(item, list):
            item = _decode_list(item)
        elif isinstance(item, dict):
            item = _decode_dict(item)
        rv.append(item)
    return rv

def _decode_dict(data):
    rv = {}
    for key, value in data.iteritems():
        if isinstance(key, unicode):
           key = key.encode('utf-8')
        if isinstance(value, unicode):
           value = value.encode('utf-8')
        elif isinstance(value, list):
           value = _decode_list(value)
        elif isinstance(value, dict):
           value = _decode_dict(value)
        rv[key] = value
    return rv


def gen_file_dict(file_path):
    return {
        'size' : os.path.getsize(file_path),
        'md5' : gen_file_md5(file_path)
    }

def gen_current_infos(file_paths):
    return {file_path:gen_file_dict(file_path) for file_path in file_paths}

def delete_none(obj):
    del obj[None]
    return obj

def get_adds(last_infos, current_infos):
    return  delete_none({(file_path if file_path not in last_infos else None):file_details
        for (file_path,file_details) in current_infos.iteritems()})

def get_dels(last_infos, current_infos):
    return  delete_none({(file_path if file_path not in current_infos else None):file_details
        for (file_path,file_details) in last_infos.iteritems()})

def get_edits(last_infos, current_infos):
    def is_exist_and_changed(file_path,file_details):
        if file_path in last_infos:
            return file_details != last_infos[file_path]
        return False
    return  delete_none({(file_path if is_exist_and_changed(file_path,file_details) else None):
        ({'new':file_details,'old':last_infos[file_path]} if is_exist_and_changed(file_path,file_details) else None)
        for (file_path,file_details) in current_infos.iteritems()})


def compare_infos(last_infos, current_infos):
    return {
        "adds" : get_adds(last_infos, current_infos),
        "dels" : get_dels(last_infos, current_infos),
        "edits" : get_edits(last_infos, current_infos)
    }


def show_diff(check_path):
    file_paths = get_all_file_paths(check_path)
    current_file_infos = gen_current_infos(file_paths)
    last_file_infos = read_from_json(result_file_path)
    diff_infos = compare_infos(last_file_infos, current_file_infos)
    return diff_infos
    # print diff_infos

def backup_file(current_file_path,backup_file_path):
    import shutil
    return shutil.copy2(current_file_path,backup_file_path)

def save_current_infos(check_path):
    backup_file(result_file_path,backup_result_file_path)
    file_paths = get_all_file_paths(check_path)
    current_file_infos = gen_current_infos(file_paths)
    write_to_json(result_file_path, current_file_infos)
    return current_infos

def test():
    file_path = os.path.realpath(__file__)
    file_md5 = gen_file_md5(file_path)
    print file_md5
    obj = {file_path:{'md5' : file_md5, 'size' : os.path.getsize(file_path)}}

    write_to_json(result_file_path, obj)
    load_obj = read_from_json(result_file_path)

    print load_obj
    print load_obj[file_path]

    print(get_all_files(check_path))


if __name__ == '__main__':
    check_path = "/Users/Colin/work/codes/python"
    print show_diff(check_path)
    # save_current_infos(check_path)