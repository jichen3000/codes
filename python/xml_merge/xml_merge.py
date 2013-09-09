from lxml import etree

def is_not_empty(value):
    return value is not None and \
        len(value.strip()) > 0

def get_xml_root(filename):
    with open(filename) as xml_file:
        return etree.parse(xml_file)

def xml_root_tostring(xml_root):
    return etree.tostring(xml_root, encoding='UTF-8',xml_declaration=True)

def get_not_empty_nodes(xml_root):
    return {xml_root.getpath(element):element.text
            for element in xml_root.iter() 
            if is_not_empty(element.text)}

def merge_to_root(origin_values, xml_root):
    changed_content = []
    for element in xml_root.iter():
        cur_path = xml_root.getpath(element)
        if cur_path in origin_values.keys() and element.text!=origin_values[cur_path]:
            changed_content.append((cur_path, element.text, origin_values[cur_path]))
            element.text = origin_values[cur_path]
    return xml_root, changed_content

def merge_files(origin_filename, target_filename, write_filename=None):
    origin_values = get_not_empty_nodes(get_xml_root(origin_filename))
    target_xml_root = get_xml_root(target_filename)
    if not write_filename: write_filename = target_filename
    changed_xml_root, changed_content = merge_to_root(origin_values, target_xml_root)
    with open(write_filename,'w') as write_xml_file:
        write_xml_file.write(xml_root_tostring(changed_xml_root))

if __name__ == '__main__':
    from minitest import *

    with test("get_not_empty_nodes"):
        origin_values = get_not_empty_nodes(get_xml_root('sample.xml'))
        origin_values.must_equal(
            {'/sample/CesiumServer': 'mservice.colin.com',
             '/sample/FileDownload/DownloadFolder': 'c:\\DOWNLOAD_FILE_DIR',
             '/sample/FileDownload/MaxRetry': '30',
             '/sample/FileUpload/DataType': 'tst',
             '/sample/FileUpload/EnableDisable': 'no',
             '/sample/FileUpload/Interval': '100',
             '/sample/FileUpload/MaxRetry': '3',
             '/sample/FileUpload/RetryElapsedTime': '100',
             '/sample/FileUpload/SourceFolder': '/folder1/dstfolder',
             '/sample/Logging/EmailOnError': 'Yes',
             '/sample/Logging/LogFileMaxSize': '10485760',
             '/sample/Logging/LogFilePath': 'c:\\sample_LOGS_DIR',
             '/sample/Logging/LogFileRotationSize': '8',
             '/sample/Logging/LogFormat': '%(asctime)s %(module)-17s line:%(lineno)-4d %(levelname)-8s %(message)s',
             '/sample/Logging/LogSystemVerbosityLimit': 'DEBUG',
             '/sample/MService/DeleteMServiceLicense_URL': 'https://colin/licensing/SoftDelete',
             '/sample/MService/GetLicenseInfo_URL': 'https://colin/licensing/GetLicenseInfo',
             '/sample/MService/GetLicense_URL': 'https://colin/licensing/LicensingResponse',
             '/sample/ServicePolicy/AdminAuthInterval': '7',
             '/sample/ServicePolicy/ServiceQuota': '12',
             '/sample/SoftwareUpgrade/AutoDownload': 'yes',
             '/sample/SoftwareUpgrade/AutoUpdate': 'yes',
             '/sample/SoftwareUpgrade/CheckInterval': '112',
             '/sample/Tandberg/WS_URL': 'https://colin/sampleServices.asmx'})

    with test("merge_to_root"):
        xml_root = get_xml_root('sample2.xml')
        changed_xml_root, changed_content = merge_to_root(origin_values, xml_root)
        changed_content.must_equal(
            [('/sample/Logging/LogFilePath', 'old2', 'c:\\sample_LOGS_DIR'),
             ('/sample/ServicePolicy/AdminAuthInterval', 'old1', '7')])
        xml_root_tostring(changed_xml_root).must_equal('''<?xml version='1.0' encoding='UTF-8'?>
<sample response="configManager">
    <CesiumServer>mservice.colin.com</CesiumServer>
    <Tandberg>
        <WS_URL>https://colin/sampleServices.asmx</WS_URL>
    </Tandberg>
    <MService>
        <GetLicense_URL>https://colin/licensing/LicensingResponse</GetLicense_URL>
        <GetLicenseInfo_URL>https://colin/licensing/GetLicenseInfo</GetLicenseInfo_URL>
        <DeleteMServiceLicense_URL>https://colin/licensing/SoftDelete</DeleteMServiceLicense_URL>
    </MService>
    <FileDownload>
      <DownloadFolder>c:\DOWNLOAD_FILE_DIR</DownloadFolder>
      <MaxRetry>30</MaxRetry>
    </FileDownload>
    <Logging>
      <LogFilePath>c:\sample_LOGS_DIR</LogFilePath>
      <LogFileRotationSize>8</LogFileRotationSize>
      <LogFileMaxSize>10485760</LogFileMaxSize>
      <LogSystemVerbosityLimit>DEBUG</LogSystemVerbosityLimit>
      <LogFormat>%(asctime)s %(module)-17s line:%(lineno)-4d %(levelname)-8s %(message)s</LogFormat>
      <EmailOnError>Yes</EmailOnError>
    </Logging>
    <ServicePolicy>
        <AdminAuthInterval>7</AdminAuthInterval>
        <ServiceQuota>12</ServiceQuota>
    </ServicePolicy>
    <ServicePolicy2>
        <AdminAuthInterval>7</AdminAuthInterval>
        <ServiceQuota>12</ServiceQuota>
    </ServicePolicy2>
</sample>''')
        pass

    with test("merge_files"):
        merge_files('sample.xml', 'sample2.xml', 'sample3.xml')