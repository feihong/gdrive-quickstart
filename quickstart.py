import httplib2
from oauth2client.service_account import ServiceAccountCredentials
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


scopes = ['https://www.googleapis.com/auth/drive.readonly']
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    'service_account_credentials.json', scopes)
credentials.authorize(httplib2.Http())
print(credentials)


gauth = GoogleAuth()
gauth.credentials = credentials

drive = GoogleDrive(gauth)

query = "mimeType = 'application/vnd.google-apps.folder'"
file_list = drive.ListFile({'q': query}).GetList()
for file1 in file_list:
  print('title: %s, id: %s' % (file1['title'], file1['id']))
