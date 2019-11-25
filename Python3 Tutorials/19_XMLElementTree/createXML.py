from lxml import etree as ET
import xml.etree.ElementTree as ET1


def _main():
    print("Creating xml")

    #create the root element
    root= ET.Element("Root_Tag")
    root.append(ET.Comment("Sample comments"))
    rootAttrib=root.attrib # references the root attribute dictionary
    rootAttrib['_attrib1']="rootAttribute1"
    rootAttrib['_attrib2']="rootAttribute2"

    #create a child1 for root
    child1 = ET.SubElement(root,"child1_Tag")
    child1Attrib=child1.attrib
    child1Attrib['_attrib1']="child1Attribute"
    child1Attrib['_attrib2']="child1Attribute"
    
    #Add comments to child1
    child1.append(ET.Comment("Child1 has details in sub child while child2 has details in attributes"))

    child2 = ET.SubElement(root,"child2_Tag")
    child2Attrib=child2.attrib
    child2Attrib['_attrib1']="child2Attribute"
    child2Attrib['_attrib2']="child2Attribute"

    #Add comments to child1
    child2.append(ET.Comment("Child1 has details in sub child while child2 has details in attributes"))

    #creating repeating subchild of child1
    child11=ET.SubElement(child1,"repeatChild1x")
    child12=ET.SubElement(child1,"repeatChild1x")
    child13=ET.SubElement(child1,"repeatChild1x")

    #filling sub childs of child11
    child111=ET.SubElement(child11,"Text")
    child111.text="Child11_Alpha"
    child112=ET.SubElement(child11,"_name")
    child112.text="Alpha"
    child113=ET.SubElement(child11,"_age")
    child113.text="21"
    #filling sub childs of child11
    child121=ET.SubElement(child12,"Text")
    child121.text="Child11_Beta"
    child122=ET.SubElement(child12,"_name")
    child122.text="Beta"
    child123=ET.SubElement(child12,"_age")
    child123.text="24"
    #filling sub childs of chil11
    child131=ET.SubElement(child13,"Text")
    child131.text="Child11_Gamma"
    child132=ET.SubElement(child13,"_name")
    child132.text="Gamma"
    child133=ET.SubElement(child13,"_age")
    child133.text="27"
 
    #creating subchild of child2
    child21=ET.SubElement(child2,"repeatChild2x")
    child22=ET.SubElement(child2,"repeatChild2x")
    child23=ET.SubElement(child2,"repeatChild2x")
    #creating text and attribute of the repeated child2x
    child21.text="child21_Alpha"
    child21.attrib['_name']="Alpha"
    child21.attrib['_age']="21"
    #creating text and attribute of the repeated child2x
    child22.text="child22_Beta"
    child22.attrib['_name']="Beta"
    child22.attrib['_age']="24"
    #creating text and attribute of the repeated child2x
    child23.text="child23_Gamma"
    child23.attrib['_name']="Gamma"
    child23.attrib['_age']="27"

    tree=ET.ElementTree(root)
    
    #file to be created
    f="./createXML.xml"

    #file open in write mode
    with open(f, 'wb') as o:
        #adding a signature to the file by doctype parameter
        #pretty_print exports well readable file
        o.write(ET.tostring(root, pretty_print=True,doctype='<?xml version="1.0" encoding="UTF-8"?>'))



def main():
    _main()

main()
