import xml.etree.ElementTree as ET


def get_data():
    ...


tree = ET.parse("nota2.xml")
root = tree.getroot()

# Print the contents of the XML file
for child in root:
    print(child.tag, child.attrib)
    for subchild in child:
        print("\t", subchild.tag, subchild.text)
