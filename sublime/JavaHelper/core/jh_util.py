
def extract_path_list(project_folders):
    return [folder_dict['path'] for folder_dict in project_folders]

def match_path(the_path, path_list):
    for cur_path in path_list:
        if the_path.find(cur_path) == 0:
            return cur_path
    return None

def mmtest(project_folders):
    print(project_folders)

if __name__ == '__main__':
    from minitest import *

    project_data = {'folders': [{'follow_symlinks': True,
          'path': '/Users/colin/work/GoogleDrive/cswork'},
         {'follow_symlinks': True, 'path': '/Users/colin/work/codes'},
         {'follow_symlinks': True, 'path': '/Users/colin/work/minitest'},
         {'follow_symlinks': True, 'path': '/Users/colin/work/colinjava'}]}


    with test(extract_path_list):
        extract_path_list(project_data['folders']).must_equal(
            ['/Users/colin/work/GoogleDrive/cswork',
             '/Users/colin/work/codes',
             '/Users/colin/work/minitest',
             '/Users/colin/work/colinjava'])

    with test(match_path):
        path_list = extract_path_list(project_data['folders'])
        the_path = '/Users/colin/work/colinjava/src/colin/ForJavatar.java'
        match_path(the_path, path_list).must_equal('/Users/colin/work/colinjava')

        the_path = '/Users/123/work/colinjava/src/colin/ForJavatar.java'
        match_path(the_path, path_list).must_equal(None)
