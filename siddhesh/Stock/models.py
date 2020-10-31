from django.db import models
import os
import requests
import bs4
import pickle
import shutil
import json
import re
from tkinter import messagebox
from itertools import repeat
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Create your models here.
class Crawl:
    def __init__(self):
        self.cmp_list=[]
        self.BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.month = ['March 15', 'March 16', 'March 17', 'March 18', 'March 19']
    def LoadList(self):
        try:
            with open(self.BASE_DIR + "//assets//cmp_list.data", 'rb') as binfile:
                self.cmp_list = pickle.load(binfile)  # read data as binary data stream
        except Exception as e:
            print('error in .bin file', e)



    def CrawlNifty50(self):
        if not os.path.exists('temp'):
            #os.mkdir(self.BASE_DIR+"//assets//temp")
            source = requests.get('https://economictimes.indiatimes.com/indices/nifty_50_companies')
            soup = bs4.BeautifulSoup(source.text, 'lxml')
            for outer in soup.find_all('p', class_='flt w120'):
                for inner in outer.find_all('a'):
                    self.cmp_list.append(inner.get('title'))

            try:
                with open(self.BASE_DIR+"//assets//cmp_list.data", 'wb') as binfile:
                    pickle.dump(self.cmp_list, binfile)  # storing data as binary data stream

            except Exception as e:
                print('MyError is', e)

        return








