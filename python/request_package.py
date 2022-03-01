import requests
import pprint

api_auth_url = "https://api.petfinder.com/v2/oauth2/token"
KEY = "UbWFPzUs8CoDW9egwI0xq2TCHSqmPcio1nFVtb1Z628RDOwCLr"
SECRET = "SWpPp6Di71i3u8YeGAYD0i4CLE6P1L88jl85zcAr"
api_url = "https://api.petfinder.com"
pbj_organization = "https://api.petfinder.com/v2/organizations/VA647"
pbj_animals = "https://api.petfinder.com/v2/animals?organization/VA647"


# headers =  {
# 	'Authorization' : f'Bearer {api_key}'
# }

#authenticate and return the token to be used for the rest of the api calls
def authenticate():
	auth_token = ""
	auth_data = {
		'grant_type' :  'client_credentials', 
		'client_id' : KEY , 
		'client_secret': SECRET 
	}
	response = requests.post(api_auth_url, data=auth_data)

	auth_token = response.json().get("access_token")
	return auth_token


#Get the url for pulling all the info on the pets
def get_org_pets_url(auth_token):
	pets_url = ""

	headers = {
		'Authorization' : f'Bearer {auth_token}' 
	}

	response = requests.get(pbj_organization, headers=headers)
	pets_url = response.json().get('organization', {}).get('_links', {}).get('animals', {}).get('href')
	return pets_url



#use the url to return an array of tuples, (animal name, url to image of animal)
def get_array_name_photo(auth_token, pets_url):
	headers = {
		'Authorization' : f'Bearer {auth_token}' 
	}
	request_for_pets_url = api_url + pets_url
	response = requests.get(request_for_pets_url, headers = headers)
	# pet_name = response.json().get()
	animals = response.json().get('animals')
	for animal in animals:
		pprint.pprint(animal.get('name'))
		pprint.pprint(animal.get('photos', {})[0].get('full'))




auth_token = authenticate()
pets_url = get_org_pets_url(auth_token)
get_array_name_photo(auth_token, pets_url)
