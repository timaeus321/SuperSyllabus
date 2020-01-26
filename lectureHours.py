# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 02:08:18 2020

@author: sunil
"""
import PyPDF2
import re
pdfFileObj = open('sample7.pdf', 'rb') 
  
# creating a pdf reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
i = 0
while(i < pdfReader.numPages-1):
    
    pageObj = pdfReader.getPage(i)
    pageText = pageObj.extractText()
    pageText = pageText.lower()
    pageText = pageText.replace(' ','')
    pageText = pageText.replace('\n','')
    lecturedaylist = []
    lecturetimelist = []
    i+=1
    result = int(pageText.find('meetingtimes'))
    lecturehours = pageText[result+34:result+60]
    ##pageText = pageText.replace('officehours:','officehours')
    if(result == -1):
        result = int(pageText.find('lectures'))
        lecturehours = pageText[result+15:result+60]
        if(result == -1):
            result = int(pageText.find('timesplaces'))
            lecturehours = pageText[result+34:result+60]
            if(result == -1):   
                continue
    
    print(lecturehours)
    lecturehourTimes =  str(''.join([i for i in lecturehours if i.isdigit()]))
    print(lecturehourTimes)
    print(len(lecturehourTimes))
    """timeFirst = False
    while(not(lecturehours[0].isalpha())):
        timeFirst = True
        lecturehours = lecturehours[1:]
    if(timeFirst):
        lecturehours = lecturehours[2:]"""
    i = 0
    
    
    while(i < len(lecturehours)):
        if(not(lecturehours[i].isalpha())):
            lecturehours = lecturehours.replace(lecturehours[i],'')
        i = i+1
    lecturehours = re.sub(r'[^a-zA-Z]', "", lecturehours)
    if(lecturehours[0:7] == 'owalkin'):
        lecturehours = lecturehours[7:]
    lecturehours = lecturehours.replace('am','')
    lecturehours = lecturehours.replace('pm','')
    lecturehours = lecturehours.lower()
    print(lecturehours)
    print(lecturehourTimes)
            
    while(1):
        if(lecturehours[0:6] == 'monday' and not('M' in lecturedaylist) ):
            lecturedaylist.append('M')
            lecturehours = lecturehours[6:]
            if(lecturehours[0:6] == 'tuesday' and not('T' in lecturedaylist) ):
                lecturedaylist.append('T')
                lecturehours = lecturehours[6:]
                if(lecturehours[0:8] == 'wednesday'and not('W' in lecturedaylist) ):
                    lecturedaylist.append('W')
                    lecturehours = lecturehours[8:]
                elif(lecturehours[0:8] == 'thursday'and not('R' in lecturedaylist) ):
                    lecturedaylist.append('R')
                    lecturehours = lecturehours[8:]
                elif(lecturehours[0:5] == 'friday' and not('F' in lecturedaylist) ):
                    lecturedaylist.append('F')
            elif(lecturehours[0:8] == 'wednesday'and not('W' in lecturedaylist) ):
                lecturedaylist.append('W')
                lecturehours = lecturehours[8:]
                if(lecturehours[0:8] == 'thursday'and not('R' in lecturedaylist) ):
                    lecturedaylist.append('R')
                    lecturehours = lecturehours[8:]
                elif(lecturehours[0:5] == 'friday'and not('F' in lecturedaylist) ):
                    lecturedaylist.append('F')
            elif(lecturehours[0:8] == 'thursday'and not('R' in lecturedaylist) ):
                lecturedaylist.append('R')
                lecturehours = lecturehours[8:]
                if(lecturehours[0:5] == 'friday'and not('F' in lecturedaylist) ):
                    lecturedaylist.append('F')
            elif(lecturehours[0:5] == 'friday'and not('F' in lecturedaylist) ):
                lecturedaylist.append('F')
        elif(lecturehours[0:7] == 'tuesday' and not('T' in lecturedaylist) ):
            lecturedaylist.append('T')
            lecturehours = lecturehours[7:]
            if(lecturehours[0:8] == 'wednesday'and not('W' in lecturedaylist) ):
                lecturedaylist.append('W')
                lecturehours = lecturehours[8:]
                if(lecturehours[0:8] == 'thursday'and not('R' in lecturedaylist) ):
                    lecturedaylist.append('R')
                    lecturehours = lecturehours[8:]
                elif(lecturehours[0:5] == 'friday'and not('F' in lecturedaylist) ):
                    lecturedaylist.append('F')
            elif(lecturehours[0:8] == 'thursday'and not('R' in lecturedaylist) ):
                lecturedaylist.append('R')
                lecturehours = lecturehours[8:]
                if(lecturehours[0:5] == 'friday'and not('F' in lecturedaylist) ):
                    lecturedaylist.append('F')
            elif(lecturehours[0:5] == 'friday'and not('F' in lecturedaylist) ):
                lecturedaylist.append('F')
        elif(lecturehours[0:8] == 'wednesday'and not('W' in lecturedaylist) ):
            lecturedaylist.append('W')
            lecturehours = lecturehours[8:]
            if(lecturehours[0:8] == 'thursday'and not('R' in lecturedaylist) ):
                lecturedaylist.append('R')
                lecturehours = lecturehours[8:]
                if(lecturehours[0:5] == 'friday'and not('F' in lecturedaylist) ):
                    lecturedaylist.append('F')
            elif(lecturehours[0:5] == 'friday'and not('F' in lecturedaylist) ):
                lecturedaylist.append('F')
        elif(lecturehours[0:8] == 'thursday'and not('R' in lecturedaylist) ):
            lecturedaylist.append('R')
            lecturehours = lecturehours[8:]
            if(lecturehours[0:5] == 'friday'and not('F' in lecturedaylist) ):
                lecturedaylist.append('F')
        elif(lecturehours[0:5] == 'friday'and not('F' in lecturedaylist) ):
            lecturedaylist.append('F')
        elif(lecturehours[0] == 'm'and not('M' in lecturedaylist) ):
            lecturedaylist.append('M')
            if(lecturehours[1] == 't' and not('T' in lecturedaylist) ):
                lecturedaylist.append('T')
                if(lecturehours[2] == 'w'and not('W' in lecturedaylist) ):
                    lecturedaylist.append('W')
                elif((lecturehours[2] == 'r' or lecturehours[2:4] == 'th') and not('R' in lecturedaylist) ):
                    lecturedaylist.append('R')
                elif(lecturehours[2] == 'f'and not('F' in lecturedaylist) ):
                    lecturedaylist.append('F')
            elif(lecturehours[1] == 'w'and not('W' in lecturedaylist) ):
                lecturedaylist.append('W')
                if((lecturehours[2] == 'r' or lecturehours[2:4] == 'th')and not('R' in lecturedaylist)) :
                    lecturedaylist.append('R')
                elif(lecturehours[2] == 'f'and not('F' in lecturedaylist) ):
                    lecturedaylist.append('F')
            elif((lecturehours[1] == 'r' or lecturehours[1:3] == 'th')and not('R' in lecturedaylist)) :
                lecturedaylist.append('R')
                if(lecturehours[2] == 'f'and not('F' in lecturedaylist) ):
                    lecturedaylist.append('F')
            elif(lecturehours[1] == 'f'and not('F' in lecturedaylist) ):
                lecturedaylist.append('F')
        elif(lecturehours[0] == 't' and not('T' in lecturedaylist) ):
            lecturedaylist.append('T')
            if(lecturehours[1] == 'w'and not('W' in lecturedaylist) ):
                lecturedaylist.append('W')
                if((lecturehours[2] == 'r' or lecturehours[2:4] == 'th') and not('R' in lecturedaylist)):
                    lecturedaylist.append('R')
                elif(lecturehours[2] == 'f'and not('F' in lecturedaylist) ):
                    lecturedaylist.append('F')
            elif((lecturehours[1] == 'r' or lecturehours[1:3] == 'th') and not('R' in lecturedaylist)):
                lecturedaylist.append('R')
                if(lecturehours[2] == 'f'and not('F' in lecturedaylist) ):
                    lecturedaylist.append('F')
            elif(lecturehours[1] == 'f'and not('F' in lecturedaylist) ):
                lecturedaylist.append('F')
        elif(lecturehours[0] == 'w'and not('W' in lecturedaylist) ):
            lecturedaylist.append('W')
            if((lecturehours[1] == 'r' or lecturehours[1:3] == 'th')and not('R' in lecturedaylist)):
                lecturedaylist.append('R')
                if(lecturehours[2] == 'f'and not('F' in lecturedaylist) ):
                    lecturedaylist.append('F')
            elif(lecturehours[1] == 'f'and not('F' in lecturedaylist) ):
                lecturedaylist.append('F')
        elif((lecturehours[0] == 'r' or lecturehours[0:2] == 'th')and not('R' in lecturedaylist)):
            lecturedaylist.append('R')
            if(lecturehours[1] == 'f'and not('F' in lecturedaylist) ):
                lecturedaylist.append('F')
        elif(lecturehours[0] == 'f'and not('F' in lecturedaylist) ):
            lecturedaylist.append('F')
        
        if(len(lecturedaylist) == 5):
            print(lecturedaylist)
            break
        if(len(lecturehours) > len(lecturedaylist)):   
            if(lecturehours[len(lecturedaylist)] == 'a' or lecturehours[len(lecturedaylist)] =='p'):
                lecturehours = lecturehours[len(lecturedaylist)+2:]
                #print(lecturehours)
                continue
        if(len(lecturehours)>1):
            if(lecturehours[1] == 'm' or lecturehours[1] =='t' or lecturehours[1] == 'w' or lecturehours[1] =='r' or lecturehours[1] == 'f'):
                lecturehours = lecturehours[1:]
                #print(lecturehours)
                continue
            if((lecturehours[0] == 'm'and not('M' in lecturedaylist)) or (lecturehours[0] == 't'and not('T' in lecturedaylist)) or (lecturehours[0] == 'w' and not('W' in lecturedaylist)) or ((lecturehours[0] == 'r' or lecturehours[0:2] == 'th') and not('R' in lecturedaylist)) or (lecturehours[0] == 'f'and not('F' in lecturedaylist))):
                #print(lecturehours)
                continue
        print(lecturedaylist)
        break
    lecturetimelist.append(lecturehourTimes[0:3])
    lecturetimelist.append(lecturehourTimes[3:6])
    print(lecturetimelist)
if(result == -1):
    print('Sorry no class meeting time could be found and read')

# closing the pdf file object 
pdfFileObj.close() 