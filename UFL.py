from collections import Counter
from bs4 import BeautifulSoup, NavigableString
import os
import requests
import urllib2
# import lxml.html
from urllib import urlopen
from urlparse import urlparse
import numpy
import itertools

import json

def get_prof_data(i):
        try:
            page_content = urlopen(i) 
        except:
            pass
        # parsed_url = urlparse(x[1])
        content = BeautifulSoup(page_content.read(), "html5lib")
        content.prettify()
        for div in content.findAll('div', {"class":"field field-name-field-research-interests-free field-type-text-long field-label-above"}):
            
            
            try:
                profdata = div.findAll(['p', 'ul'])
                print profdata
                # print "------"
            except: pass
            # try:
            #     profdata = div.findAll(['ul'])
            #     profdata = profdata.findAll('li')
            #     print profdata
            #     # print "------"
            # except: pass
            print '------'
                
                
           
            return profdata

# http://www.cis.upenn.edu/about-people/


x =  [] #to store all prof links here
#url = raw_input("Enter a website to extract the URL's from: ")
os.getenv('PORT', '8080')
os.getenv('IP', '0.0.0.0')
url = 'https://www.cise.ufl.edu/people/faculty'


r  = requests.get(url)
data = r.text
soup = BeautifulSoup(data, "html5lib")
soup.prettify()
profs = []
websites =[]


for div in soup.findAll('div',attrs={"class":"faculty-content"}):
    # print div
    professor = {}
    anchor = div.find('a')
    name = anchor.contents
    site = "https://www.cise.ufl.edu" + anchor['href']
    raw = get_prof_data(site)
    websites.append(site)
    email = anchor.find_next('a')['href']
    professor["name"] = name
    professor["site"] = site
    professor["email"] = email
    print raw
    
    profs.append(professor)
# for i in websites:
#     print i


            
            
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    