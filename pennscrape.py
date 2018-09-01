
#Importing all packages ---------------------------------------------------
from bs4 import BeautifulSoup
from urllib2 import urlopen
from datetime import timedelta, date 
import re, os #regular expression - used to search text 

#Setting dates -----------------------------------------------------------
#currdate = date(1955,10,28) #all friday papers 
#currdate = date(1958,11,15) #changes in 1958 to saturday, so need to reseed  
#currdate = date(1958,12,13) #they didn't publish on one day 
#currdate = date(1967,11,25)
#currdate = date(1970, 6,13)
#currdate = date(1971, 11, 20)
currdate = date(2001, 11, 24)

#Making array of dates --------------------------------------------------
#datestep = range(delta.days + 7) 
datestep = range(1,3001)
datearr = [] 
for z in range(0, len(datestep)): #any element i will have source year 
	currdate = currdate + timedelta(days = 7)
	datearr.append(currdate)
	print(datearr[z])

#Making array of urls -----------------------------------------------
src = []
for z in range(0, len(datestep)):
	src.append('http://panewsarchive.psu.edu/lccn/sn78001178/%s/ed-1/seq-1/ocr/' % (str (datearr[z])))
	print(src[z])

#Opening up urls, getting OCR -----------------------------------------
print(len(src))
for z in range(0, len(src)):
	print(src[z])
	try:	
		url = urlopen(src[z]).read()
	except URLError as e:
		print('FAILED TO GET FILE FOR %s' % src[z])
	else:
		soup = BeautifulSoup(url)  #puts the code of website in new element
		site = soup.find_all('breadcrumb')
		text = soup.find_all(class_='ocr_text')
		#Writing text files ------------------------------------------------------
		textout = text[0].text.encode('utf-8')
		filename = str(datearr[z]) + '.txt'
		print(filename)
		source = 'C:\\Users\\Deblina\\Downloads\\IPELab\\%s' % (filename)
		output = open(source, 'w')
		output.write(textout)
		output.close()

year = range(1982, 2018) #rang does not include ending number 

sourceYear = []
for z in range(0, len(year)): #any element i will have source year 
	sourceYear.append('http://www.presidency.ucsb.edu/satradio.php?year=%d&Submit=DISPLAY' % (year[z]))	#indexing by year you want
#making list of URLs to scrape


