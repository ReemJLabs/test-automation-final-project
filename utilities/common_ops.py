import time
import xml.etree.ElementTree as ET


def get_data(node_name):
    #Get configuration data from XML file
    root = ET.parse('C:/Users/Reem/PycharmProjects/test_automation_final_project/configuration/data.xml').getroot()
    return root.find('.//' + node_name).text

def get_time_stamp():
    return  time.time()


