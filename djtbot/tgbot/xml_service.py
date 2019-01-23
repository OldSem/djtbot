import xml.etree.ElementTree as ET


def main():
    file = 'products.xml'
    tree = ET.parse(file)
    root = tree.getroot()

    for child in root:
        print(child.tag, child.attrib)


if __name__ == "__main__":
    main()
