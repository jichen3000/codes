import os
import shutil, stat

def get_all_file_paths(file_path):
    return [os.path.join(dirpath,filename) 
        for (dirpath, dirnames, filenames) in os.walk(file_path) 
        for filename in filenames]

def isReadOnly(apath):
    return os.path.exists(apath) and (not os.access(apath, os.W_OK))

def replace_part_path(apath, src, dst):
    return dst+apath[len(src):]

def copy_file_overwrite(apath, src, dst):
    dst_file_path = replace_part_path(apath, src, dst)
    if isReadOnly(dst_file_path):
        os.chmod(dst_file_path, stat.S_IWRITE)
    if not os.path.exists(os.path.dirname(dst_file_path)):
        os.makedirs(os.path.dirname(dst_file_path))
    return shutil.copy2(apath, dst_file_path)

def copy_tree_overwrite(src, dst):
    src_all_file_paths = get_all_file_paths(src)
    return [copy_file_overwrite(cur_path, src, dst) for cur_path in src_all_file_paths]

def test():
    src = '/Users/Colin/work/test'
    dst = '/Users/Colin/work/test1'
    readonly_file_path = os.path.join(dst, 'ro.py')
    # os.chmod(readonly_file_path, stat.S_IWRITE)
    print "dirname:", os.path.dirname(dst)
    print "isReadOnly:", isReadOnly(readonly_file_path)
    print "isReadOnly:", isReadOnly(readonly_file_path+"123")
    print "isReadOnly:", isReadOnly(os.path.join(src, 'page.xhtml'))
    print get_all_file_paths(src)
    copy_tree_overwrite(src,dst)


if __name__ == '__main__':
    test()