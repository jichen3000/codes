import lxml.etree as etree

def parse_with_validation(xsd_str, xml_str):
    parser = etree.XMLParser(dtd_validation=True)
    schema_root = etree.XML(xsd_str)
    schema = etree.XMLSchema(schema_root)
    parser = etree.XMLParser(schema = schema)
    root = etree.fromstring(xml_str, parser)
    return root
    # root = etree.fromstring("<a>no int</a>", parser)

if __name__ == '__main__':
    from minitest import *
    xsd_str = '''\
        <xsd:schema xmlns:xsd="http://www.w3.org/2001/XMLSchema">
            <xsd:element name="a" type="xsd:integer"/>
        </xsd:schema>
    '''
    with test("parse_with_validation"):
        valid_xml_str = "<a>5</a>"
        root = parse_with_validation(xsd_str, valid_xml_str)
        etree.tostring(root).must_equal(valid_xml_str)

        invalid_xml_str = "<a>no int</a>"
        (lambda : parse_with_validation(xsd_str, invalid_xml_str)).must_raise(
            etree.XMLSyntaxError, "Element 'a': 'no int' is not a valid value of the atomic type 'xs:integer'.")
        
