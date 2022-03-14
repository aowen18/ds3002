#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 09:45:25 2022

@author: alexaowen
"""
#Alexa Owen
import json
import requests
import sqlite3
import pandas as pd

#Description of Project 
print ("This project pulls information from a Harry Potter API. The project gives the user information about characters in 'Harry Potter'. That information can then be converted into a CSV, JSON, or SQL file.")

#API
try:
    api_hp = requests.get ("http://hp-api.herokuapp.com/api/characters")
    hp = api_hp.json ()
except: 
    print ()
    print ("API not found")
    
#Remove unnecessary columns
df = pd.DataFrame (hp)
df = df.applymap(str)
df = df.drop ('alternate_names',1)
df = df.drop ('species',1)
df = df.drop ('gender',1)
df = df.drop ('dateOfBirth',1)
df = df.drop ('yearOfBirth',1)
df = df.drop ('eyeColour',1)
df = df.drop ('hairColour',1)
df = df.drop ('hogwartsStudent',1)
df = df.drop ('hogwartsStaff',1)
df = df.drop ('alternate_actors',1)
df = df.drop ('alive',1)
hp_df = df.drop ('image',1)

# Takes user input to select data format
print ()
file_format = input ("What format would you like your data to be in? Type 'CSV' for a CSV file, 'JSON' for a JSON file, or 'SQL' for a SQL database. Press Enter.")

#CSV input conversion
if file_format == "CSV":
    try:
        hp_df.to_csv("hp_character_info.csv")
        print ()
        print ("CSV file created")
    except: 
        print ()
        print ("CSV file unable to be created")
#JSON input conversion
elif file_format == "JSON":
    try:
        with open ("hp_character_info", "w") as outfile:
            json.dump(hp,outfile)
        print ()
        print ("JSON file created")
    except: 
        print ()
        print ("JSON file unable to be created")
#SQL input conversion
elif file_format == "SQL":
    try: 
        conn = sqlite3.connect ('hp_characters.db')
        print ()
        print ("Database Created")
    except:
        print ()
        print ("Unable to connect and create database")
    try:
        hp_df.to_sql ('character_info', conn)
        print ()
        print ("SQL table created")
    except: 
        print ()
        print ("Unable to create table")
    conn.close()
    
# Record and Column Count 
print ()
print ("Number of records:" + str(df.shape [0]))
print ("Number of columns:" +str(df.shape [1]))

