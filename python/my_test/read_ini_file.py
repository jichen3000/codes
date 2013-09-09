import ConfigParser

def read_all_items(filename):
    config = ConfigParser.RawConfigParser()
    config.read(filename)
    sections = config.sections()
    all_items = [(section, tag, value) 
            for section in sections 
            for tag, value in config.items(section)]
    return all_items

def ini_items_to_dict(items):
    return {'/'+section+'/'+tag:value for section, tag, value in items}


if __name__ == '__main__':
    from minitest import *

    with test("read_all_items"):
        items = read_all_items("test.ini")
        items.must_equal(
            [('test', 'tag1', '123'),
             ('test', 'tag2', '456'),
             ('all', 'all_tag1', 'all'),
             ('all', 'all_tag2', 'a1, a2')])

    with test("ini_items_to_dict"):
        ini_items_to_dict(items).must_equal(
            {'/all/all_tag1': 'all',
             '/all/all_tag2': 'a1, a2',
             '/test/tag1': '123',
             '/test/tag2': '456'})