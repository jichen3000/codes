import os

def compare(dir1, dir2):
    files1 = get_all_file_paths(dir1)
    files2 = get_all_file_paths(dir2)
    files1 = [file_path_sub(item, dir1) for item in files1]
    files2 = [file_path_sub(item, dir2) for item in files2]
    return (list_sub(files1, files2), list_sub(files2, files1) )

def list_sub(list_subbed, list_suber):
    return [item for item in list_subbed if item not in list_suber]

def get_all_file_paths(file_path):
    return [os.path.join(dirpath,filename) 
        for (dirpath, dirnames, filenames) in os.walk(file_path) 
        for filename in filenames]

def file_path_sub(path_subbed, path_suber):
    return path_subbed[len(path_suber):]



if __name__ == '__main__':
    dir1 = '/Users/Colin/Downloads/py_files/21'
    dir2 = '/Users/Colin/Downloads/py_files/22'
    print compare(dir1,dir2)

    # file_path = '/Users/Colin/Downloads/py_files/21/_ctypes.pyd'
    # print file_path_sub(file_path, dir1)