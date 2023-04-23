import xml.etree.ElementTree as ET
import re


def get_data(path):
    tree = ET.parse(path)
    root = tree.getroot()

    namespaces = {'nfe': 'http://www.portalfiscal.inf.br/nfe'}
    det_elements = root.findall('.//nfe:det', namespaces)

    return det_elements
    # for det in det_elements:
        # print(ET.tostring(det, encoding='utf-8').decode('utf-8'))



def clean_data(data):
    # data_string = ET.tostring(data, encoding='utf-8').decode('utf-8')
    return data.text
