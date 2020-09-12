# from urllib.request import urlopen

import pycurl
from io import BytesIO

# PBJ_pets_url="http://www.petfinder.com/search/pets-for-adoption/?shelter_id%5B0%5D=VA647&"
test_url="http://olympus.realpython.org/profiles/aphrodite"

api_url="https://api.petfinder.com/v2/oauth2/token"
api_key="NXktLE9zT6roJWfjJ6cpjTdqA0hEgALmFXKf6wZDLW3ALE3Pwj"
api_secret="AzPSef43GxJ47wCbfkDHf9wop4OYr8zRhRoJeLP6"


"""
find_new_pets

The find_new_pets function will take as input the new pets and a list of the old pets, 
go through the list and identify if there are any new pets to be added to the list.
"""


def find_new_pets():
	print('new pets placeholder')


"""
get_all_pets

This function will use the api_key to go get the information about the current
set of PBJ cats available in the system.  It will get the names and descriptions
of each pet and save them in a way that is usable in the future
"""
def get_all_pets():
	b_obj = BytesIO()
	curl=pycurl.Curl()
	curl.setopt(curl.URL, api_url)

	# post_data={ "grant_type": "client_credentials",
	# 			 "client_id": api_key,
	# 			 "client_secret": api_secret}
	curl.setopt(curl.POSTFIELDS, "grant_type=client_credentials&client_id="+api_key+"&client_secret="+api_secret)
	curl.perform()
	curl.close()
	get_body = b_obj.getvalue()
	print('Output of curl command' % get_body.decode('utf-8'))

'''
Scrape is a test function used to see if I can get access to a pages information
After further research, it looks like the petfinder api is a more reasonable approach
The API should let me find all the pets listed by PBJ, and download pictures
'''

def scrape(url):
    page = urlopen(url)
    html_bytes = page.read()
    html_out = html_bytes.decode("utf-8")
    print(html_out)


def main():
    # scrape(url)
    get_all_pets()
    # find_new_pets()
    # push_new_pets_to_slides()

if __name__ == '__main__':
    main()