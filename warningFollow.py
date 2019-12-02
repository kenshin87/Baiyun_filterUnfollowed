# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 13:12:02 2019

@author: Lenovo
"""



import pandas as pd
from idcard import id_corrected, id_15To18

from pandasHelper import pandasIterFull, pandasIterSelect, stdIdcard

# first we begin to read the people who are not standardly followed. 
s1 = pd.read_excel("s1Follow.xls")
s2 = pd.read_excel("s2Follow.xls")
s3 = pd.read_excel("s3Follow.xls")
s4 = pd.read_excel("s4Follow.xls")
wholeYearToFollowPatient = pd.read_excel("allFollow.xls")
wholeYearToFollowPatient = stdIdcard(wholeYearToFollowPatient)

print len(s1) -1 + len(s2) -1 + len(s3) -1  + len(s4) -1, 
print len(wholeYearToFollowPatient)-1

#     here we confirm that the count of the person is the same, either we 
# try to add them all, or we try to directly count the whole year data. 
assert (len(s1) -1 + len(s2) -1 + len(s3) -1  + len(s4) -1) == (len(wholeYear)-1)

# then we get the contract patient from 2nd group.  
currentSignContractPatient =  pd.read_excel(u"H:\\10010_第二团队相关工作_质控_东湖新村\\2_团队签约病人名单\\收费包二团队201911.xlsx")
currentSignContractPatientColumns = [u'身份证', u'姓名',  u'医生']
currentSignContractPatient = currentSignContractPatient[currentSignContractPatientColumns]
currentSignContractPatient = stdIdcard(currentSignContractPatient)
currentSignContractPatient[u"签约类型"] = u"基本包"


# then we get the free patient from 2nd group.  
currentSignFreePatient =  pd.read_excel(u"H:\\10010_第二团队相关工作_质控_东湖新村\\2_团队签约病人名单\\免费包二团队201911.xlsx")
currentSignFreePatientColumns = [u'证件号码', u'姓名',  u'签约医生']
currentSignFreePatient = currentSignFreePatient[currentSignFreePatientColumns]
currentSignFreePatient.columns = [u'身份证', u'姓名',  u'医生']
currentSignFreePatient = stdIdcard(currentSignFreePatient)
currentSignFreePatient[u"签约类型"] = u"免费包"

# then we try to concat and confirm that the final matrix has the same length of the previous matrix added. 
totalTable  = pd.concat([currentSignContractPatient, currentSignFreePatient])
print len(totalTable), len(currentSignContractPatient) + len(currentSignFreePatient)
assert len(totalTable) == len(currentSignContractPatient) + len(currentSignFreePatient)


totalTable.to_excel(u"第二团队总名单.xlsx", index = False)


# finally we try to filter the unfollow patient that are 
indexList = [-1]
for i,j in enumerate(totalTable[u"标准身份证"]):
    for m, n in enumerate(wholeYearToFollowPatient[u"标准身份证"]):
        if j == n:
            if i != indexList[-1]:
                indexList.append(i)
            continue
        

totalTable.iloc[indexList].to_excel(u"第二团队预警.xlsx")
