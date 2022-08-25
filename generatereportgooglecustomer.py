"""
Purpose : Google Connect is a utility to connect to the Google Search Engine.
Generate the csv data based on the search query given in the argument.
The demostrated program generate the datasheet in  a format in CSV.

Design and developed by :
Kyndryl Solutions Private Limited
Project Team : Google Cloud Platform - Guild.
Lab : Nature Labs @ Google cloud
How to use
------------
python googlecustomer.py 

Contact 
--------
Kyndryl GCP Guild Moderator : Ramamurthy V 
GCP Contact     : gcpguild@gmail.com
Date            : Aug 24 2022.
Contributors    : 90 key members from GCP Guild.
"""
from posixpath import split
import requests, re, csv, sys

import pandas as pd
from bs4 import BeautifulSoup
import bs4 as bs
import urllib.request
import numpy as np

import pandas as pd
from bs4 import BeautifulSoup
import bs4 as bs
import urllib.request
import numpy as np
import os
import sys, platform
from subprocess import check_output
from pathlib import Path

#--------------------------------------------------------------------------
def removen(string):
    for m in ('\n', '\r'):
        clean_string = re.sub(m, '', string)
        clean_string = clean_string.replace(m, '')
        clean_string = clean_string.rstrip()
        clean_string = clean_string.lstrip()
        clean_string = clean_string.strip(m)
        clean_string = re.sub(m,' ', clean_string)
        mymano = ''
        for x in clean_string:
            mymano += ''+ x
        return mymano
#---------------------------------------------------
def fullyqualifydirs(mylist):
    mydircode = N.join(mylist)
    return mydircode
#---------------------------------------------------

myos = platform.system()

if (myos == "Linux" or myos == "linux2"):
    # linux
    N="/"
    homedirectory = str(Path.home())
    
    mylist = [ homedirectory, 'serpapi/python/app/nature-labs/customerbase' ]
    basedir = fullyqualifydirs(mylist)

elif myos == "win32" or myos == "Windows":
    # Windows 
    N="\\"    
    basedir = 'C:\\serpapi\\python\\app\\nature-labs\\customerbase'  
#--------------------------------------------------------------
if not basedir:
    basedir = os.getcwd()
#-------------------------------------------------------------------------------------
mylist = [basedir, 'initialization.py'] 
initialdirectoryconfig = fullyqualifydirs(mylist)
#-------------------------------------------------------------------------------------
getdirectory = removen(check_output([sys.executable, initialdirectoryconfig], universal_newlines=True))
#-----------------------------------------------------
def mkingdirs(givenlist):
    mymanog = N.join(givenlist)
    mk_dir = Path(mymanog)
    mk_dir.mkdir(parents=True, exist_ok=True)
    return mk_dir
#-------------------------------------------------------------------
myoutdir = [basedir, 'output' ]
outputdir = mkingdirs(myoutdir)
#----------------------------------------
genlist =  [basedir, 'output' , 'Generated_Google_Cloud_report.csv']

generategooglecustomers = fullyqualifydirs(genlist)

#Google_Cloud_Customers_Report.csv
mylist = [getdirectory, 'Google_Cloud_Customers_Report.csv']
googlecustomerdata = fullyqualifydirs(mylist)

columnname = 'Google Cloud Customers'


colheader = ['Google Customer', 
'Customer business segment',
'Customer profile',
'Company Location',
'Google Cloud products',
'Coordinates'
]

def prt(p):

    width = len(p) + 4
    print('┏' + "━"*width + "┓")
    print('┃' + p.center(width) + '┃')
    print('┗' + "━"*width + "┛")
#--------------------------------------------------------------------------
pathsearchgooglecustomerdata = Path(googlecustomerdata)
if not pathsearchgooglecustomerdata.is_file():
    pi= 'Data File is missing'
    p = ("{} {}".format(pi,googlecustomerdata))
    print(p)
    exit(1)
#----------------------------------------------------
df_temples = pd.read_csv(googlecustomerdata)
#----------------------------------------------------
customer_list = df_temples.values.tolist()
#----------------------------------------------------
templeslist =  []

for t in (df_temples):
   
    if t not in templeslist:
        templeslist.append(t)
    else:
        print("Duplicate is removed", t)

def googling(query):
    inputlink = f"https://www.google.com/search?&q={search}"
    
    try:
        resp = requests.get(inputlink)
        soup = BeautifulSoup(resp.text, 'html.parser')
        gists = [x for x in soup.findAll(
                            "div", class_='BNeawe vvjwJb AP7Wnd')]
    except IndexError:
        return {"data": None, "total_items": 0}
    
    temp = []
    for r in range(0, len(gists)):
        results = gists[r].get_text()
        nd = []
        nd = [ results ]
        temp.append(nd)
    
    return {temp} 
#--------------------------------------------------------
temples_data = []

for t in customer_list:
    s = removen(''.join(str(x) for x in t))
    for l in colheader:
        search = removen("{}{}".format(l, s ))

        templestate =  [ googling(query = search) ]

        if (templestate):
            a = t +  templestate 
        
            temples_data.append(a)

gencsv = pd.DataFrame(temples_data)

pd.DataFrame(columns=colheader).to_csv(generategooglecustomers, 
mode = 'w',
index=False)
gencsv.to_csv(generategooglecustomers, header=None, index=False,
na_rep='Unknown', mode='a')

pi="\'Google Data is generated  \' :"
p = ("{} {}".format(pi,'CSV Data'))
prt(p)

pi="\'Validate the data .. !  \' :"
p = ("{} {}".format(pi,genlist))
prt(p)