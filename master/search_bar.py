'''
Created on 2017年11月16日

@author: Coder_J
'''

import tushare as ts
from urllib.request import Request


def _random(n=13):
    from random import randint
    start = 10**(n-1)
    end = (10**n)-1
    return str(randint(start, end))

def get_instrument(xapi=None):
    """
            获取证券列表
    """
    import tushare.util.conns as cs 
    xapi = cs.xapi_x() if xapi is None else xapi
    if xapi is None:
        print('服务器连接为空，请通过ts.get_apis()获取')
        return None
    data=[]
    for i in range(200): # range for python2/3
        ds = xapi.get_instrument_info(i * 300, 300)
        data += ds
        if len(ds) < 300:
            break
    data = xapi.to_df(data)
    return data

def fun1():
    cons = ts.get_apis()
    df = ts.bar(code='000001', conn=cons, start_date='2017-01-01', end_date='2017-10-31', freq='1MIN', asset='E', 
               market='',
               adj = None,
               ma = [],
               factors = [],
               retry_count = 1)
        
#     print(type(df))
#     print(df)

import requests
import pandas as pd
import numpy as np

# 00 不复权 01前复权 02后复权

def get_k_data_year(code,year,if_fq):
    data_=[]


    url='http://d.10jqka.com.cn/v2/line/hs_%s/%s/%s.js'%(str(code),str(if_fq),str(year))
    return requests.get(url).text
#     for item in requests.get(url).text.split('\"')[3].split(';'):
#         data_.append(item.split(','))
#     return pd.DataFrame(data_,index=list(np.asarray(data_).T[0]),columns=['date','open','high','low','close','volume','amount','factor'])


if __name__=='__main__':
    print(get_k_data_year('000001','2016','01'))
    print(get_k_data_year(600010,2016,'01'))



def fun3():
    conn = ts.get_apis()
    api, xapi = conn
    index_symbols = get_instrument(xapi)
    print(index_symbols)










# if __name__ == '__main__':
#     fun2()