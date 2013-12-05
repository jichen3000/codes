import xml.etree.ElementTree as ET

def write_xml(file_name):
	# build a tree structure
	root = ET.Element("html")

	head = ET.SubElement(root, "head")

	title = ET.SubElement(head, "title")
	title.text = "Page Title"
	# set an attribute
	title.attrib["class"] = "colin"

	body = ET.SubElement(root, "body")
	# or set an attribute
	body.set("bgcolor", "#ffffff")

	body.text = "Hello, World!"

	# wrap it in an ElementTree instance, and save as XML
	tree = ET.ElementTree(root)
	tree.write(file_name)


def read_xml(file_name):
	tree = ET.parse(file_name)

	# the tree root is the toplevel html element
	print "findtext",tree.findtext("head/title")
	print "findtext",tree.findtext("head/sss")

	# if you need the root element, use getroot
	root = tree.getroot()	
	print "root:",root

	for child in root.getchildren():
 		print "child:",child
 		print child.text

# write_xml("page.xhtml")
read_xml("page.xhtml")
print "ok"