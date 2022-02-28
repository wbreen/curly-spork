import requests
import pprint

api_url="https://api.petfinder.com/v2/oauth2/token"
api_key="UbWFPzUs8CoDW9egwI0xq2TCHSqmPcio1nFVtb1Z628RDOwCLr"
api_secret="idl5W4DfS3vl1RH594JCBu0r9KSuwAhxOwjE7C6E"
pbj_organization="https://api.petfinder.com/v2/organizations/VA647"
pbj_animals="https://api.petfinder.com/v2/animals?organization/VA647"


headers =  {
	'Authorization' : f'Bearer {api_key}'
}


def get_access_token():
	auth_token = ""
	return auth_token