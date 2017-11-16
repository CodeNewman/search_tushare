'''
Created on 2017年11月16日

@author: Coder_J
'''
from pytdx.hq import TdxHq_API

def s1():
    api = TdxHq_API()
    if api.connect('119.147.212.81', 7709):
    # ... same codes...
        data = api.to_df(api.get_security_bars(9, 0, '000001', 0, 5)) # 返回DataFrame
        print(data)
    
        api.disconnect()

def s2():
    api = TdxHq_API()
    with api.connect('119.147.212.81', 7709):
    # some codes
        data = api.get_security_bars(9, 0, '000001', 0, 5)
        data = api.to_df(data)
#         print(data)

if __name__ == '__main__':
#     s1()
    s2()