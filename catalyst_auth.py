#import os
from apiclient.discovery import build

#os.environ['HTTP_PROXY'] = ' '
#os.environ['HTTPS_PROXY'] = ' '

API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'
EVENTFUL_API_KEY=''


def get_authenticated_youtube():
    '''youtube connection and establishmnets 
    is performed in the same function'''
    
    print("starting connection")
    youtube = build(API_SERVICE_NAME,API_VERSION,developerKey=' ')
    print("connection established")
    return youtube