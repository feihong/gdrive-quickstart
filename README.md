# Google Drive Quickstart

## Documentation

Google Drive REST API Overview: https://developers.google.com/drive/v3/web/about-sdk

Python Quickstart: https://developers.google.com/drive/v3/web/quickstart/python

PyDrive documentation: https://github.com/googledrive/PyDrive

## Authentication

Go to [Google developer console](https://console.developers.google.com/), and follow these [directions](http://gspread.readthedocs.org/en/latest/oauth2.html).

Add the email address from the client_email field of the service account key file to the list of users who have permission to access a GDrive folder.

## Installation

```
mkvirtualenv -p python3 gdrive
pip install -r requirements.txt
```

## Notes

You can't use service accounts to authenticate to GDrive unless you are using a Google Apps domain. See [About Authorization](https://developers.google.com/drive/v3/web/about-auth).
