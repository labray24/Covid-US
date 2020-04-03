#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 09:43:21 2020

@author: pi
"""
#%% Populate namespace
import requests
import pandas as pd
import json
#%% Base Data
api_url_base = 'https://covidtracking.com/api/{}'
stderror = ("It's apparently a cluster fuck out there. Query Failed:")
#%% Base Functions
def statec():
    
    response = requests.get(api_url_base.format("states"))
    if response.status_code == 200:
        out = json.loads(response.content.decode('utf-8'))
        dfout = pd.DataFrame(out, index= out['states'])
        dfout.drop(columns=['positiveScore', 'negativeScore', 'negativeRegularScore', 'commercialScore', 'grade', 'score', 'pending', 'lastUpdateEt', 'checkTimeEt', 'dateModified', 'dateChecked', 'notes', 'hash'])
        return dfout
    else:
        print(stderror, response.status_code)
        
def stateh():
    
    response = requests.get(api_url_base.format("states/daily"))
    if response.status_code == 200:
        out = json.loads(response.content.decode('utf-8'))
        dfout = pd.DataFrame(out)
        dfout.set_index(['state','date'], inplace=True)
        return dfout
    else:
        print("Request Failed" + response.status_code)
        
def usc():
    response = requests.get(api_url_base.format("us"))
    if response.status_code == 200:
        out = json.loads(response.content.decode('utf-8'))
        dfout = pd.DataFrame(out)
        return dfout
    else:
        print("Request Failed" + response.status_code)

def ush():
   response = requests.get(api_url_base.format("us/daily"))
   if response.status_code == 200:
       out = json.loads(response.content.decode('utf-8'))
       dfout = pd.DataFrame(out)
       return dfout
   else:
       print("Request Failed" + response.status_code) 

#%% UI
def query():

   # api_url = '{0}account'.format(api_url_base)
   x = input("Please choose API endpoint\n1.States\n2.US\n")
   if x == '1':
       y = input("1.Current\n2.Historical\n")
       if y == "1":
           return statec()
       elif y == "2":
           return stateh()
       else:
           print("Selection out of Range: Just Follow Directions")
   elif x == "2":
       y = input("1.Current\n2.Historical\n")
       if y == "1":
           return usc()
       elif y == "2":
           return ush() 
       else: 
           print("Selection out of Range: Just Follow Directions")
   else:
       print("Selection out of Range: Just Follow Directions")

#%%
data = query()

#%%
        