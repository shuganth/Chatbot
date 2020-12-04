# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 12:14:22 2020

@author: Admin
"""

from bs4 import BeautifulSoup
import requests

soup = BeautifulSoup()

hospitals= {"chennai":"Rajiv Gandhi Government General Hospital",
            "vellore":"Government Vellore Medical College Hospital","salem":"Government Mohan Kumaramangalam Medical College Hospital","coimbatore":"ESI Hospital",
            "villupuram":"medical college hospital","tiruvannamalai":"tiruvannamalai Medical College Hospital","dharmapuri":"Government Dharmapuri Medical College Hospital",
            "karur":"Government Karur Medical College Hospital","chidambaram":"Raja Muthiah Medical College","tiruchi":"Mahatma Gandhi Memorial Government Hospital",
            "thanjavur":"Government Thanjavur Medical College Hospital","tiruvarur":"Government Tiruvarur Medical College Hospital","sivangaga":"Government Sivaganga Medical College Hospital",
            "madurai":"Government Madurai Medical College Hospital","theni":"Government Theni Medical College Hospital","tirunelveli":"Government Tirunelveli Medical College Hospital",
            "kanyakumari":"Government Kanyakumari Medical College Hospital"}

city="coimbatore"
for i in hospitals.keys():
    if city in i.lower():
       hospital=hospitals[i]
    
    
hospital
hospitals['coimbatore']