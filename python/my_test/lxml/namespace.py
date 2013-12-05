import lxml.etree as etree
# from lxml import etree
def pretty_xml(xml_str):
    #to print the XML so that it is readable, the function requires a file so fix it
    tree=etree.fromstring(xml_str) #pass in the xml as string 
    return etree.tostring(tree,pretty_print=True)

def parse(xml_str):
    tree = etree.fromstring(xml_str)
    # tree.nsmap['gmd'] = tree.nsmap[None]
    # tree.nsmap.pop(None)
    # ns = tree.nsmap
    # print ns
    # print "none: ",ns[None]
    # # ns.pop(None)
    # print ns
    # if you use xpath, you must remove default namespace, which key is None.
    # return tree.xpath('//ns2:ResponseMessage',namespaces=ns)[0].text
    return {'code':tree.findtext('.//{https://colin.com/schemas/common/1.0/MmtestServicesCommonSchema}ResponseCode',
        namespaces=tree.nsmap),
        'message':tree.findtext('.//{https://colin.com/schemas/common/1.0/MmtestServicesCommonSchema}ResponseMessage',
        namespaces=tree.nsmap)}



def main():
    xml_str = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<ns4:SoftDeleteResponse xmlns="https://colin.com/schemas/licensing/1.0/HostRequestParams" 
    xmlns:ns2="https://colin.com/schemas/common/1.0/MmtestServicesCommonSchema" xmlns:ns4="https://colin.com/schemas/licensing/1.0/MmtestLicensing">
  <ns2:MmtestServiceResponseHeader>
    <ns2:TrackingID>00b4360b$2013-01-16T16:10:24$00</ns2:TrackingID>
    <ns2:ResponseTimestamp>2013-01-16T08:10:30.137Z</ns2:ResponseTimestamp>
    <ns2:ResponseCode>0</ns2:ResponseCode>
    <ns2:ResponseMessage>SUCCESS</ns2:ResponseMessage>
    <ns2:TransactionID>8b671b02-1c64-45a9-afa5-e59ac4027111</ns2:TransactionID>
  </ns2:MmtestServiceResponseHeader>
  <ns4:SoftDeleteResponseBody>
    <ns4:SerialNumber>FCH16119627</ns4:SerialNumber>
    <ns4:SkuId>LDCM-MP2DPI</ns4:SkuId>
  </ns4:SoftDeleteResponseBody>
</ns4:SoftDeleteResponse>'''
    # print pretty_xml(xml_str)
    print "result:", parse(xml_str)

if __name__ == '__main__':
    main()