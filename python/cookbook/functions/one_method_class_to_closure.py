class UrlTemplate(object):
    def __init__(self, template):
        self.template = template

    def do_some(self, **kwargs):
        return "do"

def url_template(template):
    def do_some(**kwargs):
        return "do"
    return do_some

if __name__ == '__main__':
    from minitest import *

    with test(""):
        UrlTemplate("tt").do_some().must_equal("do")
        do_some = url_template("tt")
        do_some().must_equal("do")
        pass