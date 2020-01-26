# importing required modules 
import PyPDF2 
import re
# creating a pdf file object 
pdfFileObj = open('sample5.pdf', 'rb') 
  
# creating a pdf reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
  
# creating a page object
existOfficeHours = False
i = 0
while(not(existOfficeHours) and i <= pdfReader.numPages-1):
    pageObj = pdfReader.getPage(i) 
    daylist = []
    timelist = []
    # extracting text from page 
    pageText = pageObj.extractText()
    pageText = pageText.lower()
    pageText = pageText.replace(' ','')
    pageText = pageText.replace('\n','')
    result = int(pageText.find('officehours'))
    ##pageText = pageText.replace('officehours:','officehours')
    if(result != -1):
        existOfficeHours = True
        officeHours = pageText[result+11:result+60]
        officeHourTimes =  str(''.join([i for i in officeHours if i.isdigit()]))
        print(officeHourTimes)
        print(len(officeHourTimes))
        """timeFirst = False
        while(not(officeHours[0].isalpha())):
            timeFirst = True
            officeHours = officeHours[1:]
        if(timeFirst):
            officeHours = officeHours[2:]"""
        i = 0
        
        """
        while(i < len(officeHours)):
            if(not(officeHours[i].isalpha())):
                officeHours = officeHours.replace(officeHours[i],'')
            i = i+1"""
        officeHours = re.sub(r'[^a-zA-Z]', "", officeHours)
        if(officeHours[0:7] == 'owalkin'):
            officeHours = officeHours[7:]
        officeHours = officeHours.replace('am','')
        officeHours = officeHours.replace('pm','')
        for i in range(len(officeHourTimes)):
            if(int(officeHourTimes[i]) > 6 and i > 6):
                officeHourTimes = officeHourTimes.replace(officeHourTimes[i],'')
        
        print(officeHourTimes)
                
        while(1):
            if(officeHours[0:6] == 'monday' and not('M' in daylist) ):
                daylist.append('M')
                officeHours = officeHours[6:]
                if(officeHours[0:6] == 'tuesday' and not('T' in daylist) ):
                    daylist.append('T')
                    officeHours = officeHours[6:]
                    if(officeHours[0:8] == 'wednesday'and not('W' in daylist) ):
                        daylist.append('W')
                        officeHours = officeHours[8:]
                    elif(officeHours[0:8] == 'thursday'and not('R' in daylist) ):
                        daylist.append('R')
                        officeHours = officeHours[8:]
                    elif(officeHours[0:5] == 'friday' and not('F' in daylist) ):
                        daylist.append('F')
                elif(officeHours[0:8] == 'wednesday'and not('W' in daylist) ):
                    daylist.append('W')
                    officeHours = officeHours[8:]
                    if(officeHours[0:8] == 'thursday'and not('R' in daylist) ):
                        daylist.append('R')
                        officeHours = officeHours[8:]
                    elif(officeHours[0:5] == 'friday'and not('F' in daylist) ):
                        daylist.append('F')
                elif(officeHours[0:8] == 'thursday'and not('R' in daylist) ):
                    daylist.append('R')
                    officeHours = officeHours[8:]
                    if(officeHours[0:5] == 'friday'and not('F' in daylist) ):
                        daylist.append('F')
                elif(officeHours[0:5] == 'friday'and not('F' in daylist) ):
                    daylist.append('F')
            elif(officeHours[0:7] == 'tuesday' and not('T' in daylist) ):
                daylist.append('T')
                officeHours = officeHours[7:]
                if(officeHours[0:8] == 'wednesday'and not('W' in daylist) ):
                    daylist.append('W')
                    officeHours = officeHours[8:]
                    if(officeHours[0:8] == 'thursday'and not('R' in daylist) ):
                        daylist.append('R')
                        officeHours = officeHours[8:]
                    elif(officeHours[0:5] == 'friday'and not('F' in daylist) ):
                        daylist.append('F')
                elif(officeHours[0:8] == 'thursday'and not('R' in daylist) ):
                    daylist.append('R')
                    officeHours = officeHours[8:]
                    if(officeHours[0:5] == 'friday'and not('F' in daylist) ):
                        daylist.append('F')
                elif(officeHours[0:5] == 'friday'and not('F' in daylist) ):
                    daylist.append('F')
            elif(officeHours[0:8] == 'wednesday'and not('W' in daylist) ):
                daylist.append('W')
                officeHours = officeHours[8:]
                if(officeHours[0:8] == 'thursday'and not('R' in daylist) ):
                    daylist.append('R')
                    officeHours = officeHours[8:]
                    if(officeHours[0:5] == 'friday'and not('F' in daylist) ):
                        daylist.append('F')
                elif(officeHours[0:5] == 'friday'and not('F' in daylist) ):
                    daylist.append('F')
            elif(officeHours[0:8] == 'thursday'and not('R' in daylist) ):
                daylist.append('R')
                officeHours = officeHours[8:]
                if(officeHours[0:5] == 'friday'and not('F' in daylist) ):
                    daylist.append('F')
            elif(officeHours[0:5] == 'friday'and not('F' in daylist) ):
                daylist.append('F')
            elif(officeHours[0] == 'm'and not('M' in daylist) ):
                daylist.append('M')
                if(officeHours[1] == 't' and not('T' in daylist) ):
                    daylist.append('T')
                    if(officeHours[2] == 'w'and not('W' in daylist) ):
                        daylist.append('W')
                    elif((officeHours[2] == 'r' or officeHours[2:4] == 'th') and not('R' in daylist) ):
                        daylist.append('R')
                    elif(officeHours[2] == 'f'and not('F' in daylist) ):
                        daylist.append('F')
                elif(officeHours[1] == 'w'and not('W' in daylist) ):
                    daylist.append('W')
                    if((officeHours[2] == 'r' or officeHours[2:4] == 'th')and not('R' in daylist)) :
                        daylist.append('R')
                    elif(officeHours[2] == 'f'and not('F' in daylist) ):
                        daylist.append('F')
                elif((officeHours[1] == 'r' or officeHours[1:3] == 'th')and not('R' in daylist)) :
                    daylist.append('R')
                    if(officeHours[2] == 'f'and not('F' in daylist) ):
                        daylist.append('F')
                elif(officeHours[1] == 'f'and not('F' in daylist) ):
                    daylist.append('F')
            elif(officeHours[0] == 't' and not('T' in daylist) ):
                daylist.append('T')
                if(officeHours[1] == 'w'and not('W' in daylist) ):
                    daylist.append('W')
                    if((officeHours[2] == 'r' or officeHours[2:4] == 'th') and not('R' in daylist)):
                        daylist.append('R')
                    elif(officeHours[2] == 'f'and not('F' in daylist) ):
                        daylist.append('F')
                elif((officeHours[1] == 'r' or officeHours[1:3] == 'th') and not('R' in daylist)):
                    daylist.append('R')
                    if(officeHours[2] == 'f'and not('F' in daylist) ):
                        daylist.append('F')
                elif(officeHours[1] == 'f'and not('F' in daylist) ):
                    daylist.append('F')
            elif(officeHours[0] == 'w'and not('W' in daylist) ):
                daylist.append('W')
                if((officeHours[1] == 'r' or officeHours[1:3] == 'th')and not('R' in daylist)):
                    daylist.append('R')
                    if(officeHours[2] == 'f'and not('F' in daylist) ):
                        daylist.append('F')
                elif(officeHours[1] == 'f'and not('F' in daylist) ):
                    daylist.append('F')
            elif((officeHours[0] == 'r' or officeHours[0:2] == 'th')and not('R' in daylist)):
                daylist.append('R')
                if(officeHours[1] == 'f'and not('F' in daylist) ):
                    daylist.append('F')
            elif(officeHours[0] == 'f'and not('F' in daylist) ):
                daylist.append('F')
            
            if(len(daylist) == 5):
                print(daylist)
                break
            """if(timeFirst):   
                if(officeHours[len(daylist)] == 'a' or officeHours[len(daylist)] =='p'):
                    officeHours = officeHours[len(daylist)+2:]
                    #print(officeHours)
                    continue"""
            if(not(len(officeHours)==0)):
                if(officeHours[1] == 'm' or officeHours[1] =='t' or officeHours[1] == 'w' or officeHours[1] =='r' or officeHours[1] == 'f'):
                    officeHours = officeHours[1:]
                    #print(officeHours)
                    continue
                if((officeHours[0] == 'm'and not('M' in daylist)) or (officeHours[0] == 't'and not('T' in daylist)) or (officeHours[0] == 'w' and not('W' in daylist)) or ((officeHours[0] == 'r' or officeHours[0:2] == 'th') and not('R' in daylist)) or (officeHours[0] == 'f'and not('F' in daylist))):
                    #print(officeHours)
                    continue
            print(daylist)
            break
        if(len(officeHourTimes) == 4 or len(officeHourTimes) == 6):
            timelist.append(officeHourTimes[0:2])  
            timelist.append(officeHourTimes[2:])
            print(timelist)
        if(len(officeHourTimes) == 7):
            timelist.append(officeHourTimes[0:3])
            timelist.append(officeHourTimes[3:6])
            print(timelist)
        if(len(officeHourTimes) == 8):
            timelist.append(officeHourTimes[0:4])
            timelist.append(officeHourTimes[4:])
            print(timelist)
        if(len(officeHourTimes) == 11):
            timelist.append(officeHourTimes[0:3])
            timelist.append(officeHourTimes[3:5])
            timelist.append(officeHourTimes[5:8])
            timelist.append(officeHourTimes[8:11])
            print(timelist)
        if(len(officeHourTimes) == 14):
            timelist.append(officeHourTimes[0:4])
            timelist.append(officeHourTimes[4:8])
            timelist.append(officeHourTimes[8:11])
            timelist.append(officeHourTimes[11:14])
            print(timelist)
        if(len(officeHourTimes) == 16):
            timelist.append(officeHourTimes[0:4])
            timelist.append(officeHourTimes[4:8])
            timelist.append(officeHourTimes[8:12])
            timelist.append(officeHourTimes[12:16])
            print(timelist)
    i+=1
i = 0
if(len(daylist) == 0):
    print('No office hours found!')
while(i < len(timelist)):
    print(timelist[i][:1]+':'+timelist[i][1:]+'-'+timelist[i+1])
    i+=2
pdfFileObj.close() 
#######################################
#######################################
#######################################
