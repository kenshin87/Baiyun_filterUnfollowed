# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 13:41:23 2019

@author: Lenovo
"""
from idcard import id_15To18


def pandasIterFull(pandasDataframe, column = None):
    length = len(pandasDataframe)
    for i in range(length):
        print pandasDataframe.iloc[i]
    
        

def pandasIterSelect(pandasDataframe, column = None):
    length = len(pandasDataframe)
    
    if column == None:
        column = pandasDataframe.columns[0]
    
    else:
        column = column
    
    series = pandasDataframe[column]
    
    return series
        
def stdIdcard(pandasDataframe, idCardColName = None):
    if idCardColName is None:
        if u"身份证" in pandasDataframe.columns:
            pandasDataframeIdCard = pandasDataframe[u"身份证"]
        elif u"身份证号" in pandasDataframe.columns:
            pandasDataframeIdCard = pandasDataframe[u"身份证号"]
    else:
        pandasDataframeIdCard = pandasDataframe[idCardColName]
    
    pandasDataframeIdCardStd= pandasDataframeIdCard.map(id_15To18)
    
    pandasDataframe[u"标准身份证"] = pandasDataframeIdCardStd
    
    return pandasDataframe
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    