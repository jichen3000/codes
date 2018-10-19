from jinja2 import Template
import json

if __name__ == '__main__':
    from minitest import *

    with test(Template):
        template = Template('Hello {{ name }}!')
        template.render(name='John Doe').must_equal('Hello John Doe!')

    with test("file"):
        with open("temp.html") as temp_file:
            template = Template(temp_file.read())
        output = template.render(title='test html', v_dict={"data":[1,2,3,4]}, json=json)
        with open("example.html", "w") as file_:
            file_.write(output)