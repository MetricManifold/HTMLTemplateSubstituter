
import sys
import xml.etree.ElementTree as et

IN="definitions.xml"
OUT_DIR=""



def main():
	print(sys.argv)

	# read configuration
	tree = et.parse("definitions.xml")
	root = tree.getroot()

	for child in root:
		print(child.tag, child.attrib)


main()