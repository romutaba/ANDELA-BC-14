"""
This API program uses the facebook API to query a groups name, number of likes and its link
"""
import urllib.request
import json


def facebook_page_search(q):


	access_token = '1823435454578336|uioA0ZF0_JFIiU7YguiP-pPQMrE'
	# username or user_id
	page_query = q
	#pass url
	url = 'https://graph.facebook.com/'
	#pass username or user id
	page = page_query
	#combine to make final url
	final_url = url +page+'?fields=name,likes,link&access_token='+access_token
	#creates a json object from resulting response
	json_obj = urllib.request.urlopen(final_url)
	object = json_obj.read()

	return object

print(facebook_page_search("lambertselectronics"))

"""
The program requires you to have a  facebook group username or user id to execute. In 
my testing i used "lambertselectronics" 
"""