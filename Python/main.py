# from urllib.request import urlopen

import pycurl
from io import BytesIO
import json

# PBJ_pets_url="http://www.petfinder.com/search/pets-for-adoption/?shelter_id%5B0%5D=VA647&"
test_url="http://olympus.realpython.org/profiles/aphrodite"

api_url="https://api.petfinder.com/v2/oauth2/token"
api_key="NXktLE9zT6roJWfjJ6cpjTdqA0hEgALmFXKf6wZDLW3ALE3Pwj"
api_secret="AzPSef43GxJ47wCbfkDHf9wop4OYr8zRhRoJeLP6"
pbj_organization="https://api.petfinder.com/v2/organizations/VA647"
pbj_animals="https://api.petfinder.com/v2/animals?organization/VA647"
pbj_organization


"""
find_new_pets

The find_new_pets function will take as input the new pets and a list of the old pets, 
go through the list and identify if there are any new pets to be added to the list.
"""


def find_new_pets():
	print('new pets placeholder')

"""
get_access_token

returns the access token to make the request to the api with

returns the output of a json object
"""

def get_access_token():
	b_obj = BytesIO()
	curl=pycurl.Curl()
	# set url
	curl.setopt(curl.URL, api_url)
	#set output
	curl.setopt(curl.WRITEDATA, b_obj)
	# set options to add to the end, adds the credentials and key
	curl.setopt(curl.POSTFIELDS, "grant_type=client_credentials&client_id="+api_key+"&client_secret="+api_secret)
	curl.perform()
	curl.close()
	get_body = b_obj.getvalue()
	curl.close()
	json_output=json.loads(get_body)
	return json_output["access_token"]



"""
get_pet_info

returns the organization animals url ending
"""
def get_pet_info(access_token):
	b_obj = BytesIO()
	curl = pycurl.Curl()
	curl.setopt(curl.WRITEDATA, b_obj)
	curl.setopt(curl.HTTPHEADER, ["Authorization: "+ "Bearer "+ access_token])
	curl.setopt(curl.URL, pbj_animals)
	curl.perform()
	pet_list=b_obj.getvalue()
	curl.close()
	return pet_list

"""
get_all_pets

This function will use the api_key to go get the information about the current
set of PBJ cats available in the system.  It will get the names and descriptions
of each pet and save them in a way that is usable in the future

Returns a json object of all the cats
"""
def get_all_pets():
	access_token=get_access_token()
	# print(access_token)
	pets=get_pet_info(access_token)

	return pets
	
	# print('Output of curl command' % json_output)



def main():
    # scrape(url)
    get_all_pets()
    # find_new_pets()
    # push_new_pets_to_slides()

if __name__ == '__main__':
    main()