# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 17:56:11 2021

@author: Aben George

IDE: SPYDER(Variable explorer useful for webscrapping)

Credits: Manish Sharma(YouTube)
"""


import pandas as pd
import requests

# 1) DATA COLLECTION

url = 'https://en.wikipedia.org/wiki/COVID-19_pandemic_by_country_and_territory'

# 2) FILTER DATA TO GET TEXT SAVED IN TABLE FORMAT ONLY USING READ_HTML

#TO FILTER FIND THE PATH PARAMETER ASSOCIATED WITH THE TEXT ATTR
    # Ex req.text

req = requests.get(url)
data_list = pd.read_html(req.text)

# 3) USING SPYDER'S VARIABLE EXPORER
#   DOUBLE CLICK DATA_LIST AND THEN UNDER TYPE CLICK LIST
#   YOU WILL SEE ALL THE DATA FRAMES, LOOK FOR THE ONE WITH 
#   THE LARGEST SIZE, THAT MOST LIKELY WILL HAVE ALL THE COUNTRY NAMES
#   DF #2 has 239 rows, with location parameters

target_df=data_list[2]

# DATA COLLECTION END

# 4) DATA CLEANING 

        # Remove unnecessary columns, empty values, change column names,
        # Change names to remove [], delete last two rows that have text only
        # Change datatype fro int to str on 
target_df.columns=['Col0','Country Name','Total Cases', 'Total Deaths','Total Recoveries', 'Col5']

# Remove Extra Columns

target_df = target_df[['Country Name','Total Cases', 'Total Deaths','Total Recoveries']]

# Remove Extra Rows - Find Index No when exploring

#   CANT USE - target_df = target_df.drop([237, 238])- SINCE IF THE LIST ON THE WEBSITE
#           UPDATES the index # of last row will change

#   Use index[-1]
last_idx = target_df.index[-1]

target_df = target_df.drop([last_idx, last_idx-1])
# Inconsistent Country Names

    #RegularExpression - Need to write one to search for error and replace
    # \[.*\] = This Exp searches for anything within square brackets located
    # anywhere on a str

target_df['Country Name'] = target_df['Country Name'].str.replace('\[.*\]', '')
                    #replaces with empty string

# Extra/Incorrect Row Values(in col 4) to be Replaced by 0 

target_df['Total Recoveries'] = target_df['Total Recoveries'].str.replace('No data','0')
target_df['Total Cases'] = target_df['Total Cases'].str.replace('No data','0')
target_df['Total Deaths'] = target_df['Total Deaths'].str.replace('No data','0')

# Incorrect 60+ value mentioned, physically change

target_df['Total Deaths'][164] = 60


# Change Datatype of Total Cases from str to num USING pd.to_numeric

target_df['Total Cases'] = pd.to_numeric(target_df['Total Cases'])
target_df['Total Deaths'] = pd.to_numeric(target_df['Total Deaths'])
target_df['Total Recoveries'] = pd.to_numeric(target_df['Total Recoveries'])

# 5)  DATA EXPORT & ORGANIZATION

#target_df.to_csv(r'covidmanish.csv')       #WE PLACE R BEFORE FOR EASE OF READING
                                            # BY SOFTWARE
target_df.to_excel(r'covidoutput.xlsx')

