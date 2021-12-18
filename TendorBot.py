"""
TenderBot 1.0 - Casca Kwok

The bot is built in an aim to automate TCP/IP networking tendor response process, to enhance efficiency
from searching tendor parameters, just by input network equipment model into a list to save hours of effort!

TenderBot 1.0 supports information returned by .html format

Operation Manual
----------------
1.  Modify the inventory list at

eg, adding a new inventory from

inventory = ["Cisco 9400 C9400-SUP-1XL-Y", "Cisco Catalyst 9600 Series Supervisor Engine 1", "Cisco 9800-80",
             "Cisco Nexus 9500", "Cisco NCS 5500"]

to

inventory = ["Cisco 9400 C9400-SUP-1XL-Y", "Cisco Catalyst 9600 Series Supervisor Engine 1", "Cisco 9800-80",
             "Cisco Nexus 9500", "Cisco NCS 5500", "Cisco IE4000"]

2.  Modify tendor parameter.  eg, changing this line from "temperature" to "mtbf", eg, changing

SearchString = self.model.replace(" ", "+") + "+temperature"  to
SearchString = self.model.replace(" ", "+") + "+mtbf"

"""
from bs4 import BeautifulSoup
import requests
from urllib.request import Request, urlopen
import pandas as pd
import re
from re import search
import matplotlib.pyplot as plt
import numpy as np
import math
from IPython.display import display
"""

Part 1 : Obtain Cisco datasheet to obtain MTBF figure

- Web scrap MTBF figure for dataset.
    - make a google search with network equipment model name + "MTBF" as keywords
    - Take the first link returned by google
    - Download the page and search for MTBF keywords
    - print out MTBF for each network equipment
"""
#---- Part 1 : Obtain Cisco datasheet to obtain MTBF figure ------------------------------------
class Equipment: #Create objects to hold datasheet url, MTBF

    def __init__(self, equipment_model):
        self.model = equipment_model

    def DatasheetUrl(self): #function assigning datasheet url of a network equipment

        SearchString = self.model.replace(" ", "+") + "+mtbf"
        print ("Search keywords: ", SearchString)

        url1 = "https://www.google.com/search?q=" + SearchString
        req = Request(url1, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        equipment1_google = BeautifulSoup(webpage, "html.parser")
        links = equipment1_google.findAll("a", href=True)
        links2 = equipment1_google.findAll("h3")

        for items in links: #get the first url from google search result
            if (links2[0]) in items:
                result = items
                result_href = str(items.get('href'))
        try: #.html is the supported format.  .pdf might be for next version.
            result_split = result_href.replace("/url?q=", '')
            test = ".html"
            result_split = result_split[:result_split.index(test) + 5]
            print("Search Result: ", result_split, "\n")
            print("-".center(100, "-"))
            return result_split
        except:
            print ("Non .html is not supported.")


    def MtbfTable(self):
        url = self.DatasheetUrl()
        try:            #if the returned .html has "MTBF" in table
            df = pd.read_html(url, index_col=0, match='MTBF')
            return df
        except:         #else if the returned .html has no table, search by text
            req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            webpage = urlopen(req).read()
            QnA = BeautifulSoup(webpage, "html.parser")

            #soup.body.findAll(text=re.compile('^Python$'))

            mtbf = QnA.body.findAll(text=re.compile('MTBF'))

            Neat_text = ""

            for items in mtbf:
                Neat_text = Neat_text + items
            return Neat_text

#Declare a list to look up desired network equipment's MTBF
inventory = ["Cisco 9400 C9400-SUP-1XL-Y", "Cisco Catalyst 9600 Series Supervisor Engine 1", "Cisco 9800-80",
             "Cisco Nexus 9500", "Cisco NCS 5500", "Cisco IE4000"]
Cisco = {}

#automatically create objects when there is change in the list inventory
for i in range(0, len(inventory), 1):
    Cisco[i] = Equipment(inventory[i])
    print("-".center(100, "-"))
    print(Cisco[i].model.center(100), "\n", "\n")
    print("MTBF: " + "\n\n" + str(Cisco[i].MtbfTable()))
