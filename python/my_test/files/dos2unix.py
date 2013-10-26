def dos2unix(source_path, target_path=None):
    if not target_path:
        target_path = source_path
    with open(source_path,'rb') as source_file:
        text = source_file.read().replace('\r\n', '\n')
    with open(target_path,'wb') as target_file:
        target_file.write(text)
    return True

if __name__ == '__main__':
    from minitest import *
    with test("dos2unix"):
        # dos2unix('source.xml','target.xml')
        dos2unix('source.xml')
        open('source.xml','rb').read().must_equal('<test>\t\n</test>\r\n')
        open('target.xml','rb').read().must_equal('<test>\t\n</test>\n')
