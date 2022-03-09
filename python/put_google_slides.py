import requests
import pprint
import uuid
import os.path
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account


# Global variables
PRESENTATION_ID = '1RPl2YlqPdWKIfWvt-Vc3NwseYNq6SsGslSeR56-Dfuk'

gen_uuid = lambda : str(uuid.uuid4())

def authenticate_google():
    SCOPES = ['https://www.googleapis.com/auth/presentations']
    SERVICE_ACCOUNT_FILE = 'credentials.json'

    #Authenticate to the slides after 
    creds = None
    creds = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    return creds

# def 

def insert_new_slide(credentials, presentation_id, page_id):
    slides_service = build('slides', 'v1', credentials=credentials)
    requests = [
        {
            'createSlide': {
                'objectId': page_id,
                'insertionIndex': '1',
                'slideLayoutReference': {
                    'predefinedLayout': 'TITLE_AND_TWO_COLUMNS'
                }
            }
        }
    ]

    # If you wish to populate the slide with elements,
    # add element create requests here, using the page_id.

    # Execute the request.
    body = {
        'requests': requests
    }
    response = slides_service.presentations() \
        .batchUpdate(presentationId=presentation_id, body=body).execute()
    create_slide_response = response.get('replies')[0].get('createSlide')
    print('Created slide with ID: {0}'.format(
        create_slide_response.get('objectId')))

    print(response)



def main():
    credentials = authenticate_google()
    insert_new_slide(credentials, PRESENTATION_ID, gen_uuid())

if __name__ == "__main__":
    main()