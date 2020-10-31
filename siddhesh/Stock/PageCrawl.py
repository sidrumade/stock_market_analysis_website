import requests
import re
from tkinter import messagebox


class PageCrawling:
    def __init__(self):
        self.total_share_capital, self.reserves, self.debt, self.networth = 0, 0, 0, 0

    def crawl_data(self, name, url):
        print('Extract data function is called, link = ', url)
        page = requests.get(url)
        contents = str(page.content)
        contents = re.sub(r"\\r|\\n|\\t|&nbsp;", '', contents)
        try:
            f = open(fr'temp/{name}.txt', 'w+')
            f.write(contents)
            f.close()
        except Exception as e:
            messagebox.showerror('Write Error', f'cant create temp file for {name}')
