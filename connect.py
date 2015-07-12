import json, time, gdata.docs, gdata.gauth, gdata.spreadsheets.client, gdata.docs.service, gdata.spreadsheet.service, gdata.spreadsheet.text_db, re, os, sys
from oauth2client.client import SignedJwtAssertionCredentials
import urlparse
import os, sys



def connect():
    # Connect to Google
    json_key = json.load(open('JSONFILE.json'))
    scope = ['https://spreadsheets.google.com/feeds']

    credentials = SignedJwtAssertionCredentials( json_key['client_email'], json_key['private_key'], scope)
    auth2token = gdata.gauth.OAuth2TokenFromCredentials(credentials)
    client = gdata.spreadsheets.client.SpreadsheetsClient()
    auth2token.authorize(client)
    
    

    entry = gdata.spreadsheets.data.ListEntry()
    
    
    key = "SPREADSHEET_KEY"
    return entry, client, key