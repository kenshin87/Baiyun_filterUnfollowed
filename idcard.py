# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 11:13:20 2019

@author: Administrator
"""

import json
import numpy as np
import datetime as dt


def id_15To18(id_card):


    id_card = str(id_card)
    id_card = id_card.rstrip()

    if len(id_card) == 15:
        try:
            year =int(id_card[6:8])
            year_now = int(dt.datetime.now().strftime('%Y'))-2000
            if year > year_now:
                id_card_temp = id_card[0:6]+'19'+id_card[6:]   #补齐日期码
            else:
                id_card_temp = id_card[0:6]+'20'+id_card[6:]   #补齐日期码 
            
            a =np.array(list(map(int, id_card_temp)))
            b = np.array((7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2))
            last_number_temp = np.dot(a,b)%11
            check_code_list = ("1", "0", "X", "9", "8", "7", "6", "5", "4", "3", "2")
            check_code = check_code_list[last_number_temp]
            
            id_number =id_card_temp+ str(check_code)
            return id_number
        except Exception as e:
            print id_card
            param=json.dumps({"id_card":id_card})
            raise Exception({"msg":"更正用户身份证号码失败, 函数: id_corrected, 参数: "+param+", 异常信息: "+str(e)}) 

    else:
            return id_card


def id_corrected(id_card):
    """
    将老版15位身份证号码转化为新版的18位身份证号码
    逻辑：1-6位是地区号码——》保持不变
          7-12位是生日yymmdd——》转为yyyymmdd格式——》转化为17位
          添加最后一位校验码——》加权求和后关于11取余数为i——》根据校验码list，取校验码为list[i]
          前17位+校验码——》获得18位身份证号码      
    """

    id_card = str(id_card)
    id_card = id_card.rstrip()

    if len(id_card) == 18:
        return id_card
    elif id_card[0] == 'H' or  id_card[0] == 'h' or  id_card[0] == 'C' or  id_card[0] == 'U':
        return id_card
    elif len(id_card) == 15:
        try:
            year =int(id_card[6:8])
            year_now = int(dt.datetime.now().strftime('%Y'))-2000
            if year > year_now:
                id_card_temp = id_card[0:6]+'19'+id_card[6:]   #补齐日期码
            else:
                id_card_temp = id_card[0:6]+'20'+id_card[6:]   #补齐日期码 
            
            a =np.array(list(map(int, id_card_temp)))
            b = np.array((7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2))
            last_number_temp = np.dot(a,b)%11
            check_code_list = ("1", "0", "X", "9", "8", "7", "6", "5", "4", "3", "2")
            check_code = check_code_list[last_number_temp]
            
            id_number =id_card_temp+ str(check_code)
            return id_number
        except Exception as e:
            print id_card
            param=json.dumps({"id_card":id_card})
            raise Exception({"msg":"更正用户身份证号码失败, 函数: id_corrected, 参数: "+param+", 异常信息: "+str(e)}) 

    else:
            print id_card
            raise Exception({"msg":"更正用户身份证号码失败, 函数: id_corrected, 参数: "+param+", 异常信息: "+str(e)}) 
            

 