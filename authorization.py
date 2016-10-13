import httplib2
from oauth2client.service_account import ServiceAccountCredentials


scopes = ['https://www.googleapis.com/auth/drive.readonly']
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    'service_account_credentials.json', scopes)
credentials.authorize(httplib2.Http())
print(credentials)
