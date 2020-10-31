from django.http import JsonResponse
import json
from django.shortcuts import render
from .models import Crawl
import pickle
import os
import sqlite3
from django.views.generic import View




# Create your views here. function

        
    


def index(request):
    obj = Crawl()
    obj.CrawlNifty50()  # find nifty50
    return render(request,'index.html')

def home(request):
    return render(request,'Home.html')#here can pass data as dict or object

def singlegraph(request):
    value1 = request.COOKIES.get('username')
    if value1 is None:
        print('cookies1 not set')
        try:
            value2 = request.COOKIES['username']
            print('cookie is ', value2)
            conn=sqlite3.connect('MyData.db')
            cursor=conn.execute(f"SELECT * FROM MYDATA WHERE COMPANY_NAME = '{value2}'")
            tsc=[]
            res=[]
            net=[]
            debt=[]
            for row in cursor:
                tsc.append(row[1])
                res.append(row[2])
                net.append(row[3])
                debt.append(row[4])
            conn.close()
            context={'cmp_name':value2,'tsc':tsc,'res':res,'net':net,'debt':debt}
            print(context)
            return render(request,'singlegraph.html',context)
        except KeyError:
            print('cookies2 not set')
    else:
        conn=sqlite3.connect('MyData.db')
        cursor=conn.execute(f"SELECT * FROM MYDATA WHERE COMPANY_NAME = '{value1}'")
        tsc=[]
        res=[]
        net=[]
        debt=[]
        for row in cursor:
            tsc.append(row[1])
            res.append(row[2])
            net.append(row[3])
            debt.append(row[4])
        conn.close()
        context={'cmp_name':value1,'tsc':tsc,'res':res,'net':net,'debt':debt}
        print(context)
        return render(request,'singlegraph.html',context)



def shownifty50(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    cmp_list_Extra=[]
    try:
        with open(Crawl().BASE_DIR+"//assets//cmp_list.data", 'rb') as binfile:
            cmp_listP = pickle.load(binfile)  # read data as binary data stream

    except Exception as e:
        print('error is here:', e)   # messagebox.showwarning('IO Error', 'close cmp_list.txt')

    f = open(BASE_DIR + "//assets//CompanyLinks.json")  # all urls
    d = json.load(f)
    cmp_list = list(d.keys())
    for i in cmp_listP:
        if i not in cmp_list:
            cmp_list_Extra.append(i)
    print(cmp_list_Extra)

    Extra=len(cmp_list_Extra)>0 #gives true false
    return render(request, 'shownifty50.html', {'cmp_list':cmp_list,'cmp_list_Extra':cmp_list_Extra,'Extra':Extra})






