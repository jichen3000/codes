def __handle_node_without_attrs(node):
    if(len(node)==0):
        content = node.text
    else:
        content = __handle_parent_node_without_attrs(node)
    return (node.tag, content)

def __handle_parent_node_without_attrs(node):
    return tuple((__handle_node_without_attrs(element) for element in node))

def __handle_node_with_attrs(node):    
    attrs = None
    if(len(node)==0):
        content = node.text
    else:
        content = __handle_parent_node_with_attrs(node)
    if(len(node.attrib)>0):
        attrs = tuple((key, value) for key,value in node.attrib.items())
    return (node.tag, (("CONTENT", content), ("ATTRS", attrs)))

def __handle_parent_node_with_attrs(node):
    return tuple((__handle_node_with_attrs(element) for element in node))


def __trans_value(value):
    if type(value) == tuple:
        return tuple_to_dict(value)
    else:
        return value

def tuple_to_dict(lst):
    result_dict = {}
    for key, value in lst:
        transed_value = __trans_value(value)
        if key in result_dict:
            previouse_one = result_dict[key]
            if type(previouse_one) == list:
                previouse_one.append(transed_value)
            else:
                result_dict[key] = [previouse_one, transed_value]
        else:
            result_dict[key] = transed_value        
    return result_dict

def xml_to_tuple(xml_doc, with_attrs=False):
    if with_attrs:
        return __handle_parent_node_with_attrs(xml_doc)
    else:
        return __handle_parent_node_without_attrs(xml_doc)

def xml_to_dict(xml_doc, with_attrs=False):
    xml_lst = xml_to_tuple(xml_doc, with_attrs)
    return tuple_to_dict(xml_lst)

class XmlDict(dict):
    @classmethod
    def create(cls, xml_doc):
        this = cls()
        content_dict = xml_to_dict(xml_doc, with_attrs=True)
        print content_dict
        this.__dict__ = content_dict
        return this


if __name__ == '__main__':
    from minitest import *

    try:
        import xml.etree.cElementTree as ET
    except ImportError:
        import xml.etree.ElementTree as ET
    contents='''\
<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Status>OK</Status>
  <CountryCode local='world' type='11'>US</CountryCode>
  <CountryName>United States</CountryName>
  <Message>
    <Id>1</Id>
    <Content>I'm ok!</Content>
  </Message>
  <Message other='true'>
    <Id>2</Id>
    <Content>continue</Content>
  </Message>
</Response>'''
    doc=ET.fromstring(contents)

    with test("XmlDict"):
        xml_dict = XmlDict.create(doc)
        print xml_dict.Status

    with test("xml_to_dict without_attrs"):
        xml_to_tuple(doc).must_equal(
            (('Status', 'OK'),
             ('CountryCode', 'US'),
             ('CountryName', 'United States'),
             ('Message', (('Id', '1'), ('Content', "I'm ok!"))),
             ('Message', (('Id', '2'), ('Content', 'continue'))))
            )
        xml_to_dict(doc).must_equal(
            {'CountryCode': 'US',
             'CountryName': 'United States',
             'Message': [{'Content': "I'm ok!", 'Id': '1'},
                         {'Content': 'continue', 'Id': '2'}],
             'Status': 'OK'})
    with test("xml_to_dict with_attrs"):
        xml_to_tuple(doc, with_attrs=True).must_equal(
            (('Status', (('CONTENT', 'OK'), ('ATTRS', None))),
             ('CountryCode',
              (('CONTENT', 'US'), ('ATTRS', (('type', '11'), ('local', 'world'))))),
             ('CountryName', (('CONTENT', 'United States'), ('ATTRS', None))),
             ('Message',
              (('CONTENT',
                (('Id', (('CONTENT', '1'), ('ATTRS', None))),
                 ('Content', (('CONTENT', "I'm ok!"), ('ATTRS', None))))),
               ('ATTRS', None))),
             ('Message',
              (('CONTENT',
                (('Id', (('CONTENT', '2'), ('ATTRS', None))),
                 ('Content', (('CONTENT', 'continue'), ('ATTRS', None))))),
               ('ATTRS', (('other', 'true'),)))))
            )
        xml_to_dict(doc, with_attrs=True).must_equal(
            {'CountryCode': {'ATTRS': {'local': 'world', 'type': '11'}, 'CONTENT': 'US'},
             'CountryName': {'ATTRS': None, 'CONTENT': 'United States'},
             'Message': [{'ATTRS': None,
                          'CONTENT': {'Content': {'ATTRS': None, 'CONTENT': "I'm ok!"},
                                      'Id': {'ATTRS': None, 'CONTENT': '1'}}},
                         {'ATTRS': {'other': 'true'},
                          'CONTENT': {'Content': {'ATTRS': None, 'CONTENT': 'continue'},
                                      'Id': {'ATTRS': None, 'CONTENT': '2'}}}],
             'Status': {'ATTRS': None, 'CONTENT': 'OK'}})

    with test("xpath"):
        doc.findall(".").size().must_equal(1)
        doc.find(".").tag.must_equal("Response")

        doc.find("./Message/Id").text.must_equal("1")
        doc.findall("./Message/Id").size().must_equal(2)
