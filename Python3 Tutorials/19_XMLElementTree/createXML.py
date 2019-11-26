from lxml import etree as ET
import uuid


def _main():

    #create the root element
    root= ET.Element("School")
    root.append(ET.Comment("Structure of School"))
    rootAttrib=root.attrib # references the root attribute dictionary
    rootAttrib['Name']="Oxford public school"
    rootAttrib['Location']="Maryland, IN"

    #create a child1 for root - sub elements are list
    faculty     = ET.SubElement(root,"Faculty")

    #principal details
    principal       = ET.SubElement(faculty, "Principal")
    principal.attrib['Grade']="A-grade"
    principal.attrib['_uuid']=str(uuid.uuid4())
    principalname   = ET.SubElement(principal,"Name")
    principalname.text ="Alexander Dimetri"
    principalage    = ET.SubElement(principal,"Age")
    principalage.text="54"
    principalQualification = ET.SubElement(principal, "Qualification")
    principalQualification.text="PhD, M.Sc, B.Sc"

    #Senior Faculty details
    seniorFaculty = ET.SubElement(faculty, "Senior_Faculty")
    seniorFaculty.attrib['Grade']="A-grade"

    seniorFaculty1 = ET.SubElement(seniorFaculty, "Senior_Faculty_1")
    seniorFaculty1.attrib['EmploymentType']="Full Time"
    seniorFaculty1.attrib['_uuid']=str(uuid.uuid4())
    seniorFaculty1Name= ET.SubElement(seniorFaculty1, "Name")
    seniorFaculty1Name.text = "Mrs. Samantha Pitroda"
    seniorFaculty1Age   = ET.SubElement(seniorFaculty1,"Age")
    seniorFaculty1Age.text = "48"
    seniorFaculty1Qualification = ET.SubElement(seniorFaculty1, "Qualification")
    seniorFaculty1Qualification.text = "Phd , M.Ed"

    seniorFaculty2 = ET.SubElement(seniorFaculty, "Senior_Faculty_2")
    seniorFaculty2.attrib['EmploymentType']="Full Time"
    seniorFaculty2.attrib['_uuid']=str(uuid.uuid4())
    seniorFaculty2Name= ET.SubElement(seniorFaculty2, "Name")
    seniorFaculty2Name.text = "Mrs. Pauline John"
    seniorFaculty2Age   = ET.SubElement(seniorFaculty2,"Age")
    seniorFaculty2Age.text = "52"
    seniorFaculty2Qualification = ET.SubElement(seniorFaculty2, "Qualification")
    seniorFaculty2Qualification.text = "M.Phil, M.Ed"

    seniorFaculty3 = ET.SubElement(seniorFaculty, "Senior_Faculty_3")
    seniorFaculty3.attrib['EmploymentType']="Visiting Faculty"
    seniorFaculty3.attrib['_uuid']=str(uuid.uuid4())
    seniorFaculty3Name= ET.SubElement(seniorFaculty3, "Name")
    seniorFaculty3Name.text = "Mrs. Iris Chua"
    seniorFaculty3Age   = ET.SubElement(seniorFaculty3,"Age")
    seniorFaculty3Age.text = "53"
    seniorFaculty3Qualification = ET.SubElement(seniorFaculty3, "Qualification")
    seniorFaculty3Qualification.text = "M.Ed"


    #Other Faculty details
    otherFaculty = ET.SubElement(faculty, "Other_Faculty")
    otherFaculty.attrib['Grade']="B-grade"

    otherFaculty1 = ET.SubElement(otherFaculty, "Other_Faculty_1")
    otherFaculty1.attrib['EmploymentType']="Full Time"
    otherFaculty1.attrib['_uuid']=str(uuid.uuid4())
    otherFaculty1Name= ET.SubElement(otherFaculty1, "Name")
    otherFaculty1Name.text = "Mrs. Andrea Michael"
    otherFaculty1Age   = ET.SubElement(otherFaculty1,"Age")
    otherFaculty1Age.text = "32"
    otherFaculty1Qualification = ET.SubElement(otherFaculty1, "Qualification")
    otherFaculty1Qualification.text = "M.Ed"

    otherFaculty2 = ET.SubElement(otherFaculty, "Other_Faculty_2")
    otherFaculty2.attrib['EmploymentType']="Full Time"
    otherFaculty2.attrib['_uuid']=str(uuid.uuid4())
    otherFaculty2Name= ET.SubElement(otherFaculty2, "Name")
    otherFaculty2Name.text = "Mrs. Norman Thomas"
    otherFaculty2Age   = ET.SubElement(otherFaculty2,"Age")
    otherFaculty2Age.text = "37"
    otherFaculty2Qualification = ET.SubElement(otherFaculty2, "Qualification")
    otherFaculty2Qualification.text = "B.Ed"

    otherFaculty3 = ET.SubElement(otherFaculty, "Senior_Faculty_3")
    otherFaculty3.attrib['EmploymentType']="Part time"
    otherFaculty3.attrib['_uuid']=str(uuid.uuid4())
    otherFaculty3Name= ET.SubElement(otherFaculty3, "Name")
    otherFaculty3Name.text = "Mrs. Gabriella John"
    otherFaculty3Age   = ET.SubElement(otherFaculty3,"Age")
    otherFaculty3Age.text = "43"
    otherFaculty3Qualification = ET.SubElement(otherFaculty3, "Qualification")
    otherFaculty3Qualification.text = "M.Ed"

    #Class details
    grades    = ET.SubElement(root,"Grade")

    #Grade details

    grade1 = ET.SubElement(grades, "Grade1")
    grade1.attrib['GradeType']="Senior Secondary"
    grade1.attrib['_uuid']=str(uuid.uuid4())
    grade1Name= ET.SubElement(grade1, "Grade_Teacher")
    grade1Name.text = "Mrs. Andrea Michael"
    grade1Age   = ET.SubElement(grade1,"Class_Strength")
    grade1Age.text = "35"

    grade2 = ET.SubElement(grades, "Grade2")
    grade2.attrib['GradeType']="High School"
    grade2.attrib['_uuid']=str(uuid.uuid4())
    grade2Name= ET.SubElement(grade2, "Grade_Teacher")
    grade2Name.text = "Mrs. Norman Thomas"
    grade2Age   = ET.SubElement(grade2,"Class_Strength")
    grade2Age.text = "37"

    grade3 = ET.SubElement(grades, "Grade3")
    grade3.attrib['GradeType']="Primary"
    grade3.attrib['_uuid']=str(uuid.uuid4())
    grade3Name= ET.SubElement(grade3, "Grade_Teacher")
    grade3Name.text = "Mrs. Gabriella John"
    grade3Age   = ET.SubElement(grade3,"Class_Strength")
    grade3Age.text = "31"




    """
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
    """
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
