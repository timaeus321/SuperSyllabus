# importing required modules 
import PyPDF2 
  
# creating a pdf file object 
pdfFileObj = open('sample3.pdf', 'rb') 
  
# creating a pdf reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
  
# creating a page object
existOfficeHours = False
i = 0
while(not(existOfficeHours) and i <= pdfReader.numPages-1):
    pageObj = pdfReader.getPage(i) 
    daylist = []
    daylist.append('F')
    # extracting text from page 
    pageText = pageObj.extractText()
    pageText = pageText.lower()
    pageText = pageText.replace(' ','')
    pageText = pageText.replace('\n','')
    result = int(pageText.find('officehours'))
    ##pageText = pageText.replace('officehours:','officehours')
    if(result != -1):
        existOfficeHours = True
        officeHours = pageText[result+12:result+54]
        print(officeHours)
        if(officeHours[0:6] == 'monday'):
            daylist.append('M')
            if(officeHours[6:12] == 'tuesday'):
                daylist.append('T')
                if(officeHours[13:21] == 'wednesday'):
                    daylist.append('W')
                elif(officeHours[13:21] == 'thursday'):
                    daylist.append('R')
                elif(officeHours[13:18] == 'friday'):
                    daylist.append('F')
            elif(officeHours[6:14] == 'wednesday'):
                daylist.append('W')
                if(officeHours[15:23] == 'thursday'):
                    daylist.append('R')
                elif(officeHours[15:20] == 'friday'):
                    daylist.append('F')
            elif(officeHours[6:14] == 'thursday'):
                daylist.append('R')
                if(officeHours[15:20] == 'friday'):
                    daylist.append('F')
            elif(officeHours[6:11] == 'friday'):
                daylist.append('F')
        elif(officeHours[0:7] == 'tuesday'):
            daylist.append('T')
            if(officeHours[6:14] == 'wednesday'):
                daylist.append('W')
                if(officeHours[15:23] == 'thursday'):
                    daylist.append('R')
                elif(officeHours[15:20] == 'friday'):
                    daylist.append('F')
            elif(officeHours[6:14] == 'thursday'):
                daylist.append('R')
                if(officeHours[15:20] == 'friday'):
                    daylist.append('F')
            elif(officeHours[6:11] == 'friday'):
                daylist.append('F')
        elif(officeHours[0:8] == 'wednesday'):
            daylist.append('W')
            if(officeHours[6:14] == 'thursday'):
                daylist.append('R')
                if(officeHours[15:20] == 'friday'):
                    daylist.append('F')
            elif(officeHours[6:11] == 'friday'):
                daylist.append('F')
        elif(officeHours[0:8] == 'thursday'):
            daylist.append('R')
            if(officeHours[6:11] == 'friday'):
                daylist.append('F')
        elif(officeHours[0:5] == 'friday'):
            daylist.append('F')
        elif(officeHours[0] == 'm'):
            daylist.append('M')
            if(officeHours[1] == 't'):
                daylist.append('T')
                if(officeHours[2] == 'w'):
                    daylist.append('W')
                elif(officeHours[2] == 't'):
                    daylist.append('R')
                elif(officeHours[2] == 'f'):
                    daylist.append('F')
            elif(officeHours[1] == 'w'):
                daylist.append('W')
                if(officeHours[2] == 't'):
                    daylist.append('R')
                elif(officeHours[2] == 'f'):
                    daylist.append('F')
            elif(officeHours[1] == 't'):
                daylist.append('R')
                if(officeHours[2] == 'f'):
                    daylist.append('F')
            elif(officeHours[1] == 'f'):
                daylist.append('F')
        elif(officeHours[0] == 't'):
            daylist.append('T')
            if(officeHours[1] == 'w'):
                daylist.append('W')
                if(officeHours[2] == 't'):
                    daylist.append('R')
                elif(officeHours[2] == 'f'):
                    daylist.append('F')
            elif(officeHours[1] == 't'):
                daylist.append('R')
                if(officeHours[2] == 'f'):
                    daylist.append('F')
            elif(officeHours[1] == 'f'):
                daylist.append('F')
        elif(officeHours[0] == 'w'):
            daylist.append('W')
            if(officeHours[1] == 't'):
                daylist.append('R')
                if(officeHours[2] == 'f'):
                    daylist.append('F')
            elif(officeHours[1] == 'f'):
                daylist.append('F')
        elif(officeHours[0] == 't'):
            daylist.append('R')
            if(officeHours[1] == 'f'):
                daylist.append('F')
        elif(officeHours[0] == 'f'):
            daylist.append('F')
        print(daylist)
    i = i+1

# closing the pdf file object 
pdfFileObj.close() 