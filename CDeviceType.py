# coding:utf-8
'''
Created on 2020-10-14

@author: Dizzy
'''

from enum import Enum

class CDeviceType(Enum):
    OtherFactory_OtherType = 1
    H3C_ER3200G2 = 2
    
class CDeviceVersion(Enum):
    OtherFactory_OtherHardware_OtherSoftwareVersion = 1
    H3C_ERHMG2_MNW100_R1118 = 2
    
class CAPTemplateType(Enum):
    OtherApTemplate = 1
    AP_TEMPLATE_1_149 = 2
    AP_TEMPLATE_6_153 = 3
    AP_TEMPLATE_11_157 = 4
