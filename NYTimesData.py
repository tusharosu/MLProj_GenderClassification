#install BeautifulSoup Library

from urllib2 import Request, urlopen, URLError
from BeautifulSoup import BeautifulSoup
import urllib, sys
import urllib2
from HTMLParser import HTMLParser
from cookielib import CookieJar
import json
Days=[28,31,30,31,30,31,31,30,31,30,31]
report=[]
firstname = ""
NameList= ""
for j in range (1,11):
    i=j+1
    if i%10==i:
        Month="0"+str(i)
    else:
        Month=str(i)
    Days1=Days[j];
    for f in range (1,Days1):
            if f%10==f:
	        Day="0"+str(f)
	    else:
                Day=str(f)
            date1="2012"+Month+Day
	    requestStr = "http://api.nytimes.com/svc/search/v2/articlesearch.json?facet_field=day_of_week&begin_date="+str(date1)+"&end_date="+str(date1)+"&api-key=e6964ee273a0578697ec4e5b15fdf399:1:71765563"
	    request=Request(requestStr)
	    try:		           
		   response = urlopen(request)
		   json_object = json.load(response)
		   if not(json_object is None):
		       l = list(json_object.values())[1]
		       m = list(l.values())[0]
		       for b in m:
			   web_url = list(b.values())[11]
			   print NameList.find(str(web_url))
			   if NameList.find(str(web_url)) == -1:			           
				   k=list(b.values())[15]
				   if not(k is None) and not(len(k)==0):
					   pr = list(k.values())[0]
					   for j in pr:
					       if hasattr(j,"values") and len(list(j.values())) >=4:				
							  firstname=list(j.values())[3]
							  if not(firstname == 1):
							          NameList=NameList+str(web_url)
								  cj = CookieJar()
								  opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
								  p = opener.open(web_url)
								  encoding = p.headers.getparam('charset')
								  html = p.read().decode(encoding)
								  soup = BeautifulSoup(html)
								  for row in soup.findAll("div",attrs={"class" : "entry-content"}):
									report.append(row.getText().strip().encode('utf8'))
								  if not("video") in web_url:
								          file1=open("Data1.txt","a")
									  file1.write(str(firstname))
									  file1.write("\n\n\n")
									  file1.write(str(report))
									  file1.write("\n\n\n")
									  file1.write(str(web_url))
									  file1.write("\n\n\n")
									  report=[]
	   
	    except URLError, e:
		print 'Got an error code:', e
		raw_input()
	    NameList=""
raw_input()
