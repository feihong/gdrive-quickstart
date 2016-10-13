import httplib2
from oauth2client.service_account import ServiceAccountCredentials
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


scopes = ['https://www.googleapis.com/auth/drive.readonly']
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    'service_account_credentials.json', scopes)
credentials.authorize(httplib2.Http())

gauth = GoogleAuth()
gauth.credentials = credentials
drive = GoogleDrive(gauth)

# query = "mimeType = 'application/vnd.google-apps.folder'"
query = "title = 'Shipping Label Inbox'"
directory = drive.ListFile({'q': query}).GetList()[0]
dir_id = directory['id']

query = "'{}' in parents".format(dir_id)
file_list = drive.ListFile({'q': query}).GetList()
print('{} files in directory'.format(len(file_list)))
for fil in file_list:
  print('title: {}, id: {}'.format(fil['title'], fil['id']))
