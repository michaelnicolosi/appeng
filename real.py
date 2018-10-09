
# importing the requests library 
import requests 

endpoint = 'https://google-analytics.com/collect?v=1&t=event&tid=UA-121324737-1&cid=43789789.23578678&ec=appengine&ea=mm-protocol&el=some-test'
  
# sending post request and saving response as response object 
r = requests.post(url = endpoint) 
