import urllib.request
import urllib.parse
import re
import os
import datetime


url = 'https://kops.uni-konstanz.de/handle/123456789/44776'
req = urllib.request.Request(url)
resp = urllib.request.urlopen(req)
respData = resp.read()

#<td class="ds-table-cell even datacell">35</td>
paragraphs = re.findall(r'<td(.*?)</td>',str(respData))
    
numberdwl = paragraphs[-1]
numberdwl = re.findall(r'\d',numberdwl)
numberdwl = ''.join(numberdwl)
numberdwl = int(numberdwl)

cwd = os.getcwd()
now = datetime.datetime.now()
today = str(now.year) + '.' + str(now.month) + '.' + str(now.day)

# Ask if number in string

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

os.chdir('D:\\2-Beruf\PhD\Dissertation\Download_History')

# Ask if file exists...

if not os.path.isfile('./NumDownloadsDiss2.txt'):
    print('File does not exist. It is written the first entry.')
    title = 'History of Number of Downloads of my dissertation\n\nDate - Number of Downloads'
    saveFile = open('NumDownloadsDiss2.txt','w')
    saveFile.write(title)
    saveFile.close()

"""
 If the file exists already then:
 1. Find out what is the date of the last line in the file
 2. If the last entry is from today, then do nothing,
    otherwise make an entry 'Date - NumberDownloads'
"""

if os.path.isfile('./NumDownloadsDiss2.txt'):
    print('The file exists already')
    print('Date of today:',today)

    readFile = open('NumDownloadsDiss2.txt','r').readlines()
    if hasNumbers(readFile[-1]):
        lastline = re.findall(r'\d{1,4}',readFile[-1])
        lastdateentry = lastline[0] + '.' + lastline[1] + '.' + lastline[2]
        last_numberdwlEntry = lastline[-1]
    else:
        lastdateentry = '0'
        last_numberdwlEntry = '0'
        
if (lastdateentry != today and last_numberdwlEntry != str(numberdwl)):
 
    appendMe = '\n'+ today + ' - ' + str(numberdwl)
    saveFile = open('NumDownloadsDiss2.txt','a')
    saveFile.write(appendMe)
    saveFile.close()


