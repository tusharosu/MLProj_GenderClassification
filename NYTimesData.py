from urllib2 import Request, urlopen, URLError
import json
Days=[31,28,31,30,31,30,31,31,30,31,30,31]
for j in range (0,11):
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
	           file1=open("Data1.txt","a")
		   response = urlopen(request)
		   json_object = json.load(response)
		   if not(json_object is None):
		       l = list(json_object.values())[1]
		       m = list(l.values())[0]
		       for b in m:
			   web_url = list(b.values())[11]
			   k=list(b.values())[15]
			   if not(k is None) and not(len(k)==0):
				   pr = list(k.values())[0]
				   for j in pr:
				       if hasattr(j,"values") and len(list(j.values())) >=4:
				          firstname=list(j.values())[3]
				          file1.write(str(web_url))
				          file1.write("    ")
				          file1.write(str(firstname))
				          file1.write("::")
				          print web_url	
				          print firstname
	    except URLError, e:
		print 'Got an error code:', e
		raw_input()
raw_input()
